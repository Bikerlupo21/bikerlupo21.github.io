"""
Template grafiche Bikerlupo: schizzo a matita su foglio bianco.

Regole di stile (dalla guida Bikerlupo):
- foglio #FBFAF6 con grana leggera e vignettatura calda appena accennata
- tratto grafite #2B2B2B irregolare, ogni segmento ripassato 2 volte con piccolo tremolio,
  opacità 0,5-0,9, spessore variabile
- testi scritti a mano in Caveat 700, MAI sottolineati
- cerchi a mano libera con 1,1 giri, frecce con asta leggermente curva + due tratti di punta
- timbro del logo BL21 in basso a destra (~140 px, opacità 85%)
- unico colore extra ammesso: celeste del brand #38B6FF, come "matita colorata"

Uso:
    from matita import Foglio
    f = Foglio(1600, 1000, seme=1)
    f.linea([(100, 100), (500, 120)])
    f.testo(300, 200, "aspirazione", 48)
    f.salva_png("public/img/motore/esempio.png")
"""
from __future__ import annotations

import base64
import math
import random
from pathlib import Path

GRAFITE = "#2B2B2B"
CARTA = "#FBFAF6"
CELESTE = "#38B6FF"

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent.parent
FONT_CAVEAT = RADICE / "node_modules/@fontsource/caveat/files/caveat-latin-700-normal.woff2"
LOGO = RADICE / "public/img/bl21-logo-a-small.png"


def _b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode()


class Foglio:
    def __init__(self, larghezza: int, altezza: int, seme: int = 21, timbro: bool = True):
        self.w, self.h = larghezza, altezza
        self.r = random.Random(seme)
        self.el: list[str] = []
        self.timbro = timbro

    # ---------- tratti di base ----------
    def _trema(self, pts, ampiezza):
        """Aggiunge punti intermedi con un leggero tremolio della mano."""
        out = []
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            d = math.hypot(x2 - x1, y2 - y1)
            n = max(2, int(d / 18))
            for i in range(n):
                t = i / n
                out.append((x1 + (x2 - x1) * t + self.r.uniform(-ampiezza, ampiezza),
                            y1 + (y2 - y1) * t + self.r.uniform(-ampiezza, ampiezza)))
        out.append((pts[-1][0] + self.r.uniform(-ampiezza, ampiezza), pts[-1][1] + self.r.uniform(-ampiezza, ampiezza)))
        return out

    @staticmethod
    def _path(pts, chiuso=False):
        # curva morbida (Catmull-Rom -> Bezier) per un tratto "a mano"
        if len(pts) < 3:
            d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f} " + " ".join(f"L{x:.1f},{y:.1f}" for x, y in pts[1:])
        else:
            d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f} "
            for i in range(len(pts) - 1):
                p0 = pts[i - 1] if i > 0 else pts[i]
                p1, p2 = pts[i], pts[i + 1]
                p3 = pts[i + 2] if i + 2 < len(pts) else p2
                c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
                c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
                d += f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} "
        return d + ("Z" if chiuso else "")

    def linea(self, pts, spessore=3.2, colore=GRAFITE, passate=2, ampiezza=1.4, chiuso=False):
        """Linea a matita: ripassata `passate` volte, ognuna con tremolio e opacità diverse."""
        if chiuso:
            pts = list(pts) + [pts[0]]
        for _ in range(passate):
            p = self._trema(pts, ampiezza)
            op = self.r.uniform(0.55, 0.9)
            sw = spessore * self.r.uniform(0.75, 1.15)
            self.el.append(f'<path d="{self._path(p)}" fill="none" stroke="{colore}" stroke-width="{sw:.2f}" '
                           f'stroke-linecap="round" stroke-linejoin="round" opacity="{op:.2f}"/>')

    def rettangolo(self, x, y, w, h, **kw):
        # angoli leggermente sporgenti, come a mano libera
        e = 6
        self.linea([(x - e, y), (x + w + e, y)], **kw)
        self.linea([(x + w, y - e), (x + w, y + h + e)], **kw)
        self.linea([(x + w + e, y + h), (x - e, y + h)], **kw)
        self.linea([(x, y + h + e), (x, y - e)], **kw)

    def ellisse(self, cx, cy, rx, ry, giri=1.1, **kw):
        """Ellisse a mano libera: 1,1 giri con sovrapposizione finale."""
        n = 48
        start = self.r.uniform(0, math.tau)
        pts = []
        for i in range(int(n * giri) + 1):
            a = start + math.tau * i / n
            k = 1 + 0.03 * math.sin(a * 3 + start)
            pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
        self.linea(pts, **kw)

    def freccia(self, x1, y1, x2, y2, curva=0.12, punta=22, **kw):
        """Asta leggermente curva + due tratti per la punta."""
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = x2 - x1, y2 - y1
        cx, cy = mx - dy * curva, my + dx * curva
        pts = [((1 - t) ** 2 * x1 + 2 * (1 - t) * t * cx + t * t * x2,
                (1 - t) ** 2 * y1 + 2 * (1 - t) * t * cy + t * t * y2) for t in [i / 12 for i in range(13)]]
        self.linea(pts, **kw)
        a = math.atan2(y2 - pts[-3][1], x2 - pts[-3][0])
        for s in (-1, 1):
            b = a + math.pi - s * 0.45
            self.linea([(x2 + punta * math.cos(b), y2 + punta * math.sin(b)), (x2, y2)], **kw)

    def tratteggio(self, x, y, w, h, passo=14, angolo=-35, colore=GRAFITE, spessore=1.6):
        """Ombreggiatura a tratteggio dentro un rettangolo (gas, ombre). angolo: inclinazione dei tratti."""
        if h <= 4 or w <= 4:
            return
        k = h / math.tan(math.radians(abs(angolo))) * (1 if angolo > 0 else -1)
        clip = f"c{len(self.el)}"
        self.el.append(f'<clipPath id="{clip}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath><g clip-path="url(#{clip})">')
        i = -abs(k) - passo
        while i < w + abs(k) + passo:
            self.linea([(x + i, y + h + 4), (x + i + k, y - 4)], spessore=spessore, colore=colore, passate=1, ampiezza=0.8)
            i += passo
        self.el.append("</g>")

    def scintilla(self, cx, cy, r=26, **kw):
        for k in range(8):
            a = k * math.tau / 8 + self.r.uniform(-0.15, 0.15)
            lung = r if k % 2 == 0 else r * 0.6
            self.linea([(cx + math.cos(a) * 6, cy + math.sin(a) * 6), (cx + math.cos(a) * lung, cy + math.sin(a) * lung)], **kw)

    def testo(self, x, y, s, dim=40, colore=GRAFITE, ancora="middle", ruota=None):
        rot = self.r.uniform(-1.5, 1.5) if ruota is None else ruota
        s = s.replace("&", "&amp;").replace("<", "&lt;")
        self.el.append(f'<text x="{x}" y="{y}" font-family="Caveat" font-weight="700" font-size="{dim}" '
                       f'fill="{colore}" text-anchor="{ancora}" opacity="0.92" transform="rotate({rot:.2f} {x} {y})">{s}</text>')

    # ---------- uscita ----------
    def svg(self) -> str:
        font = f"@font-face{{font-family:'Caveat';src:url(data:font/woff2;base64,{_b64(FONT_CAVEAT)}) format('woff2');font-weight:700;}}"
        carta = (f'<filter id="grana"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7"/>'
                 f'<feColorMatrix values="0 0 0 0 0.42  0 0 0 0 0.38  0 0 0 0 0.3  0 0 0 0.07 0"/></filter>'
                 f'<radialGradient id="vign" cx="50%" cy="50%" r="75%"><stop offset="70%" stop-color="#000" stop-opacity="0"/>'
                 f'<stop offset="100%" stop-color="#8a6a3a" stop-opacity="0.10"/></radialGradient>')
        timbro = ""
        if self.timbro and LOGO.exists():
            tw = 140
            th = tw * 185 / 400
            timbro = (f'<image href="data:image/png;base64,{_b64(LOGO)}" x="{self.w - tw - 34}" y="{self.h - th - 28}" '
                      f'width="{tw}" height="{th:.0f}" opacity="0.85" transform="rotate(-4 {self.w - tw / 2 - 34} {self.h - th / 2 - 28})"/>')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">'
                f'<defs><style>{font}</style>{carta}</defs>'
                f'<rect width="100%" height="100%" fill="{CARTA}"/>'
                f'<rect width="100%" height="100%" filter="url(#grana)"/>'
                f'<rect width="100%" height="100%" fill="url(#vign)"/>'
                + "".join(self.el) + timbro + "</svg>")

    def salva_png(self, percorso: str | Path):
        """Renderizza con Chrome headless (Playwright) e salva PNG."""
        from playwright.sync_api import sync_playwright
        percorso = Path(percorso)
        percorso.parent.mkdir(parents=True, exist_ok=True)
        html = f"<html><body style='margin:0'>{self.svg()}</body></html>"
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
            pg = b.new_page(viewport={"width": self.w, "height": self.h})
            pg.set_content(html)
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(percorso), clip={"x": 0, "y": 0, "width": self.w, "height": self.h})
            b.close()
        return percorso

"""Schizzi per "Cilindrata, alesaggio e corsa" e "Coppia e potenza". Avvio: python3 strumenti/schizzi/basi.py"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, RADICE, Foglio  # noqa: E402

USCITA = RADICE / "public/img/motore"


def quota_o(f, x1, x2, y, testo, sopra=True):
    """Quota orizzontale con frecce alle estremità."""
    f.freccia((x1 + x2) / 2, y, x1, y, curva=0, punta=14, spessore=2)
    f.freccia((x1 + x2) / 2, y, x2, y, curva=0, punta=14, spessore=2)
    f.testo((x1 + x2) / 2, y - 16 if sopra else y + 40, testo, 34)


def quota_v(f, x, y1, y2, testo):
    f.freccia(x, (y1 + y2) / 2, x, y1, curva=0, punta=14, spessore=2)
    f.freccia(x, (y1 + y2) / 2, x, y2, curva=0, punta=14, spessore=2)
    f.testo(x + 22, (y1 + y2) / 2 + 12, testo, 34, ancora="start")


def cilindrata():
    f = Foglio(1440, 900, seme=41)
    f.testo(720, 70, "alesaggio, corsa e cilindrata", 56)
    # cilindro con pistone al PMI e linea del PMS
    xl, xr, top, bot = 330, 650, 210, 690
    f.linea([(xl, top - 40), (xl, bot + 60)], spessore=3.4)
    f.linea([(xr, top - 40), (xr, bot + 60)], spessore=3.4)
    f.linea([(xl - 30, top - 40), (xr + 30, top - 40)], spessore=3.4)
    pms, pmi = top + 40, bot - 110
    f.tratteggio(xl + 6, pms, xr - xl - 12, pmi - pms, passo=12, colore=CELESTE, spessore=2)
    for y in range(int(xl), int(xr), 28):
        f.linea([(y, pms), (y + 14, pms)], spessore=1.8, passate=1)
    f.rettangolo(xl + 8, pmi, xr - xl - 16, 110, spessore=3.2)
    f.testo(xl - 20, pms + 10, "PMS", 34, ancora="end")
    f.testo(xl - 20, pmi + 10, "PMI", 34, ancora="end")
    quota_o(f, xl, xr, top - 70, "alesaggio (diametro del cilindro)")
    quota_v(f, xr + 50, pms, pmi, "corsa")
    f.testo((xl + xr) / 2, (pms + pmi) / 2 + 10, "cilindrata", 40)
    f.testo((xl + xr) / 2, (pms + pmi) / 2 + 52, "unitaria", 40)
    # formula ed esempio a destra
    X = 830
    f.testo(X, 330, "cilindrata unitaria =", 40, ancora="start")
    f.testo(X, 385, "π × (alesaggio/2)² × corsa", 40, ancora="start")
    f.testo(X, 470, "× numero di cilindri", 40, ancora="start")
    f.testo(X, 525, "= cilindrata totale", 40, ancora="start")
    f.testo(X, 640, "es. 80 × 60 mm, un cilindro:", 34, ancora="start")
    f.testo(X, 685, "3,1416 × 40² × 60 = 301.593 mm³", 34, ancora="start")
    f.testo(X, 730, "≈ 301,6 cm³", 40, ancora="start")
    return f.salva_png(USCITA / "cilindrata-alesaggio-corsa.png")


def rapporti():
    f = Foglio(1440, 760, seme=43)
    f.testo(720, 70, "stessa cilindrata, forme diverse", 56)
    # dimensioni scelte perché diametro² × altezza sia (quasi) uguale: stesso volume
    casi = (("sottoquadro", "corsa lunga", 170, 367), ("quadro", "alesaggio = corsa", 220, 220), ("superquadro", "corsa corta", 290, 126))
    for i, (nome, sotto, w, h) in enumerate(casi):
        cx = 260 + i * 460
        base = 560
        f.linea([(cx - w / 2, base - h), (cx - w / 2, base)], spessore=3.2)
        f.linea([(cx + w / 2, base - h), (cx + w / 2, base)], spessore=3.2)
        f.linea([(cx - w / 2, base), (cx + w / 2, base)], spessore=3.2)
        f.linea([(cx - w / 2, base - h), (cx + w / 2, base - h)], spessore=2, passate=1)
        f.tratteggio(cx - w / 2 + 6, base - h + 4, w - 12, h - 8, passo=12, colore=CELESTE, spessore=2)
        f.testo(cx, base + 60, nome, 44)
        f.testo(cx, base + 104, sotto, 34)
    f.testo(720, 720, "il volume (la cilindrata) è lo stesso: cambiano diametro e altezza", 32)
    return f.salva_png(USCITA / "alesaggio-corsa-rapporto.png")


def coppia_potenza():
    f = Foglio(1440, 860, seme=47)
    f.testo(720, 70, "coppia e potenza", 58)
    # sinistra: coppia = forza x braccio
    cx, cy = 330, 470
    f.ellisse(cx, cy, 40, 40, spessore=3)
    f.linea([(cx, cy), (cx + 260, cy - 20)], spessore=7)
    f.freccia(cx + 260, cy - 150, cx + 260, cy - 30, curva=0, punta=20, colore=CELESTE, spessore=4)
    f.testo(cx + 270, cy - 170, "forza", 40)
    quota_o(f, cx, cx + 260, cy + 60, "braccio", sopra=False)
    a0, a1 = math.radians(200), math.radians(320)
    f.freccia(cx + 90 * math.cos(a0), cy + 90 * math.sin(a0), cx + 90 * math.cos(a1), cy + 90 * math.sin(a1), curva=-0.3, punta=16, spessore=2.6)
    f.testo(cx + 60, 250, "coppia = forza × braccio", 42)
    f.testo(cx + 60, 700, "quanto \"tira\" l'albero (Nm)", 36)
    # destra: potenza = coppia x giri
    f.linea([(720, 160), (722, 780)], spessore=1.4, passate=1)
    X = 1080
    f.testo(X, 250, "potenza = coppia × giri", 42)
    for k, (y, giri) in enumerate(((410, "piano"), (590, "veloce"))):
        f.ellisse(X - 140, y, 60, 60, spessore=3)
        f.linea([(X - 140, y), (X - 92, y - 30)], spessore=5)
        n = 1 if k == 0 else 3
        for j in range(n):
            a = math.radians(-40 + j * 32)
            f.freccia(X - 140 + 85 * math.cos(a - 0.5), y + 85 * math.sin(a - 0.5), X - 140 + 85 * math.cos(a), y + 85 * math.sin(a), curva=-0.2, punta=12, spessore=2.2)
        f.testo(X + 40, y - 6, "stessa coppia", 34, ancora="start")
        f.testo(X + 40, y + 34, f"gira {giri}" + (": più potenza" if k else ""), 34, ancora="start")
    f.testo(X, 760, "kW = Nm × giri/min ÷ 9549", 38)
    return f.salva_png(USCITA / "coppia-potenza.png")


if __name__ == "__main__":
    for fn in (cilindrata, rapporti, coppia_potenza):
        print(fn())

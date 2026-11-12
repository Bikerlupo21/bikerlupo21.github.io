"""Copertina "Il motore": monocilindrico 4 tempi in sezione (schema semplificato). Avvio: python3 strumenti/schizzi/motore_completo.py"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, RADICE, Foglio  # noqa: E402


def arco(cx, cy, r, a0, a1, n=24, ry=None):
    ry = ry or r
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def tondo_rett(x, y, w, h, r):
    p = []
    p += arco(x + w - r, y + r, r, -90, 0, 6)
    p += arco(x + w - r, y + h - r, r, 0, 90, 6)
    p += arco(x + r, y + h - r, r, 90, 180, 6)
    p += arco(x + r, y + r, r, 180, 270, 6)
    return p


def etichetta(f, x_testo, y_testo, x_pt, y_pt, testo, ancora="start"):
    f.testo(x_testo, y_testo, testo, 36, ancora=ancora, ruota=0)
    xa = x_testo - 12 if ancora == "start" else x_testo + 12
    f.linea([(xa, y_testo - 12), (x_pt, y_pt)], spessore=1.6, passate=1, ampiezza=0.8)
    f.ellisse(x_pt, y_pt, 5, 5, spessore=1.6, passate=1)


def disegna():
    f = Foglio(1600, 900, seme=33)
    cx = 640

    # carter (basamento) con albero motore
    f.linea(tondo_rett(430, 560, 420, 290, 90), spessore=3.6, chiuso=True)
    ccy = 715
    f.ellisse(cx, ccy, 105, 105, spessore=3)          # volantino / contrappeso
    f.ellisse(cx, ccy, 22, 22, spessore=2.6)          # asse
    f.ellisse(cx, ccy, 34, 34, spessore=1.8, passate=1)  # pignone distribuzione
    t = math.radians(40)
    px, py = cx + 70 * math.sin(t), ccy - 70 * math.cos(t)
    f.ellisse(px, py, 16, 16, spessore=2.4)           # perno di biella

    # cilindro alettato
    top, base = 300, 565
    f.linea([(545, top), (545, base)], spessore=3.4)
    f.linea([(735, top), (735, base)], spessore=3.4)
    for y in range(top + 14, base - 6, 22):
        f.linea([(470, y), (545, y)], spessore=2.2, passate=1)
        f.linea([(735, y), (810, y)], spessore=2.2, passate=1)
    f.linea([(470, top + 14), (470, base - 18)], spessore=1.6, passate=1)
    f.linea([(810, top + 14), (810, base - 18)], spessore=1.6, passate=1)

    # pistone e biella
    L = 255
    spin = py - math.sqrt(L * L - (70 * math.sin(t)) ** 2)
    ptop = spin - 38
    f.rettangolo(552, ptop, 176, 88, spessore=3.2)
    f.linea([(556, ptop + 14), (724, ptop + 14)], spessore=1.6)
    f.linea([(556, ptop + 26), (724, ptop + 26)], spessore=1.6)
    f.ellisse(cx, spin, 13, 13, spessore=2.2)
    f.linea([(cx, spin), (px, py)], spessore=6)
    f.tratteggio(551, 222, 178, ptop - 228, passo=11, colore=CELESTE, spessore=1.8)

    # testata alettata
    f.linea(tondo_rett(495, 200, 290, 102, 18), spessore=3.4, chiuso=True)
    for y in range(214, 296, 20):
        f.linea([(455, y), (495, y)], spessore=2, passate=1)
        f.linea([(785, y), (825, y)], spessore=2, passate=1)
    f.linea([(552, 300), (728, 300)], spessore=2.6)

    # coperchio distribuzione, albero a camme e corona
    f.linea(tondo_rett(530, 60, 220, 142, 40), spessore=3.2, chiuso=True)
    f.ellisse(cx, 130, 62, 62, spessore=2.4)          # corona (doppia del pignone: l'albero a camme gira a metà)
    f.linea(arco(cx, 130, 22, 0, 360, 20, 30), spessore=3, chiuso=False)  # lobo della camma
    f.ellisse(cx, 130, 9, 9, spessore=2, passate=1)

    # valvole a V
    for s in (-1, 1):
        x_alto, x_basso = cx + s * 30, cx + s * 62
        f.linea([(x_alto, 168), (x_basso, 292)], spessore=3)
        f.linea([(x_basso - 30, 298), (x_basso + 30, 298)], spessore=3.4)
        for k in range(4):
            yy = 200 + k * 12
            xx = x_alto + (x_basso - x_alto) * (yy - 168) / 124
            f.linea([(xx - 14, yy), (xx + 14, yy + 6)], spessore=1.6, passate=1)  # molla

    # catena di distribuzione (tratteggiata: passa dietro al cilindro)
    for s in (-1, 1):
        x1, x2 = cx + s * 34, cx + s * 62
        for i in range(0, 20, 2):
            a, b = i / 20, (i + 1) / 20
            f.linea([(x1 + (x2 - x1) * a, ccy + (130 - ccy) * a), (x1 + (x2 - x1) * b, ccy + (130 - ccy) * b)],
                    spessore=1.8, passate=1, ampiezza=0.6)

    # candela
    f.linea([(735, 215), (790, 175)], spessore=2.6)
    f.linea([(748, 230), (803, 190)], spessore=2.6)
    f.linea([(790, 175), (803, 190)], spessore=2.6)
    f.linea([(803, 190), (830, 165)], spessore=4)

    # aspirazione (sinistra) e scarico (destra)
    f.linea([(560, 290), (500, 240), (380, 240)], spessore=2.8)
    f.linea([(600, 300), (520, 280), (380, 280)], spessore=2.8)
    f.rettangolo(300, 225, 80, 72, spessore=2.6)
    f.freccia(220, 262, 290, 262, curva=0, punta=16, colore=CELESTE, spessore=3)
    f.linea([(680, 300), (780, 280), (870, 300), (930, 380), (960, 500)], spessore=2.8)
    f.linea([(720, 300), (790, 250), (900, 270), (980, 360), (1010, 500)], spessore=2.8)

    # titolo
    f.testo(60, 640, "il motore,", 54, ancora="start", ruota=-2)
    f.testo(60, 700, "pezzo per pezzo", 54, ancora="start", ruota=-2)
    f.testo(62, 770, "monocilindrico 4 tempi", 32, ancora="start", ruota=-1)
    f.testo(62, 810, "schema semplificato", 32, ancora="start", ruota=-1)

    # etichette (colonna destra)
    X = 1110
    etichetta(f, X, 100, 662, 130, "albero a camme")
    etichetta(f, X, 165, 785, 205, "candela")
    etichetta(f, X, 230, 694, 262, "valvole")
    etichetta(f, X, 295, 790, 240, "testata")
    etichetta(f, X, 360, 950, 430, "scarico")
    etichetta(f, X, 425, 800, 470, "cilindro alettato")
    etichetta(f, X, 490, 724, ptop + 20, "pistone e fasce")
    etichetta(f, X, 555, 683, 560, "catena di distribuzione")
    etichetta(f, X, 620, (cx + px) / 2 + 8, (spin + py) / 2, "biella")
    etichetta(f, X, 685, 737, 760, "albero motore")
    etichetta(f, X, 750, 830, 800, "carter")
    # etichetta sinistra
    f.testo(340, 340, "aspirazione", 36, ruota=0)
    f.linea([(340, 312), (340, 300)], spessore=1.6, passate=1)

    return f.salva_png(RADICE / "public/img/motore/motore-completo.png")


if __name__ == "__main__":
    print(disegna())

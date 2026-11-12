"""Schizzi della pagina Chi sono. Avvio: python3 strumenti/schizzi/chi_sono.py"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, GRAFITE, RADICE, Foglio  # noqa: E402

USCITA = RADICE / "public/img/chi-sono"


def moto(f, cx, cy, s=1.0, scooter=False, colore=GRAFITE):
    """Moto generica vista di lato (non un modello reale)."""
    r = 34 * s
    f.ellisse(cx - 70 * s, cy, r, r, spessore=2.6, colore=colore)
    f.ellisse(cx + 70 * s, cy, r, r, spessore=2.6, colore=colore)
    if scooter:
        f.linea([(cx - 70 * s, cy), (cx - 40 * s, cy - 40 * s), (cx + 40 * s, cy - 40 * s), (cx + 50 * s, cy - 10 * s)], spessore=2.6, colore=colore)
        f.linea([(cx + 70 * s, cy), (cx + 55 * s, cy - 90 * s), (cx + 40 * s, cy - 100 * s)], spessore=2.6, colore=colore)
        f.linea([(cx - 60 * s, cy - 40 * s), (cx - 40 * s, cy - 60 * s), (cx + 10 * s, cy - 60 * s), (cx + 20 * s, cy - 40 * s)], spessore=2.4, colore=colore)
    else:
        f.linea([(cx - 70 * s, cy), (cx - 20 * s, cy - 40 * s), (cx + 40 * s, cy - 40 * s), (cx + 70 * s, cy)], spessore=2.6, colore=colore)
        f.linea([(cx + 70 * s, cy), (cx + 45 * s, cy - 80 * s), (cx + 30 * s, cy - 90 * s)], spessore=2.6, colore=colore)
        f.linea([(cx - 20 * s, cy - 40 * s), (cx - 10 * s, cy - 70 * s), (cx + 40 * s, cy - 75 * s), (cx + 40 * s, cy - 40 * s)], spessore=2.4, colore=colore)
        f.linea([(cx - 75 * s, cy - 55 * s), (cx - 10 * s, cy - 70 * s)], spessore=2.4, colore=colore)


def strada():
    f = Foglio(1440, 760, seme=301)
    f.testo(720, 70, "la mia strada in moto", 56)
    pts = [(80 + 1280 * i / 100, 400 + 28 * math.sin(i / 100 * math.tau * 2)) for i in range(101)]
    f.linea(pts, spessore=4)
    f.linea([(x, y + 22) for x, y in pts], spessore=2, passate=1)
    tappe = [
        ("14 anni", "Liberty 50", "smontato mille volte", True),
        ("la maturità", "l'incidente", "e lo stop ai motori", None),
        ("28 anni", "Z750 del 2006", "la prima moto vera", False),
        ("poi", "MT-09 del 2014", "giri e Toscana con papà", False),
        ("oggi", "CBR 600 RR del 2010", "la pista con Luca Feltri", False),
    ]
    for k, (quando, cosa, nota, tipo) in enumerate(tappe):
        x = 190 + k * 265
        y = 400 + 28 * math.sin((x - 80) / 1280 * math.tau * 2)
        f.ellisse(x, y + 11, 11, 11, spessore=2.4, colore=CELESTE)
        if tipo is None:
            f.scintilla(x, y - 90, r=38, spessore=2)
        else:
            moto(f, x, y - 60, s=0.75, scooter=tipo, colore=CELESTE if k == 4 else GRAFITE)
        f.testo(x, y + 90, quando, 28)
        f.testo(x, y + 130, cosa, 30)
        f.testo(x, y + 164, nota, 22)
    f.testo(720, 700, "e la passione, intanto, non si è mai fermata", 32)
    return f.salva_png(USCITA / "la-mia-strada.png")


def garage():
    f = Foglio(1440, 820, seme=303)
    f.testo(720, 70, "l'altra metà del sogno", 56)
    f.linea([(120, 700), (1320, 700)], spessore=3)
    f.linea([(160, 700), (160, 200), (720, 130), (1280, 200), (1280, 700)], spessore=3.4)
    for i in range(1, 6):
        f.linea([(160, 200 + i * 6), (1280, 200 + i * 6)], spessore=0.8, passate=1)
    for k, cx in enumerate((330, 600, 870, 1140)):
        moto(f, cx, 630, s=1.0, colore=CELESTE if k == 1 else GRAFITE)
    f.rettangolo(250, 300, 240, 120, spessore=2.4)
    for i in range(6):
        f.linea([(270 + i * 36, 320), (270 + i * 36, 400)], spessore=1.6, passate=1)
    f.testo(370, 450, "attrezzi", 28)
    f.rettangolo(1000, 290, 200, 130, spessore=2.4)
    f.testo(1100, 365, "BL21", 44)
    f.testo(720, 770, "un garage pieno di moto", 34)
    return f.salva_png(USCITA / "garage-dei-sogni.png")


if __name__ == "__main__":
    USCITA.mkdir(parents=True, exist_ok=True)
    for fn in (strada, garage):
        print(fn())

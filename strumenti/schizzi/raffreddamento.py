"""Schizzi del gruppo Lubrificazione e raffreddamento. Avvio: python3 strumenti/schizzi/raffreddamento.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, GRAFITE, RADICE, Foglio  # noqa: E402
from manovellismo import etichetta  # noqa: E402

USCITA = RADICE / "public/img/motore"


def olio():
    f = Foglio(1440, 1000, seme=91)
    f.testo(720, 70, "il giro dell'olio (carter umido)", 56)
    # sagoma motore
    f.linea([(300, 160), (300, 600), (1000, 600), (1000, 160), (300, 160)], spessore=3)
    f.linea([(300, 300), (1000, 300)], spessore=1.4, passate=1)
    f.testo(650, 230, "testata: alberi a camme", 32)
    f.ellisse(500, 450, 70, 70, spessore=2.6)
    f.testo(500, 560, "albero motore", 30)
    f.ellisse(820, 450, 50, 50, spessore=2.4)
    f.ellisse(900, 470, 34, 34, spessore=2.2)
    f.testo(860, 560, "cambio e frizione", 30)
    # coppa
    f.linea([(300, 600), (360, 780), (940, 780), (1000, 600)], spessore=3)
    f.tratteggio(352, 700, 596, 76, passo=12, colore=CELESTE, spessore=1.3)
    f.linea([(340, 700), (960, 700)], spessore=1.6, passate=1, colore=CELESTE)
    f.testo(650, 830, "coppa: l'olio torna giù per gravità", 32)
    # pescante, pompa, filtro, canali
    f.linea([(420, 760), (420, 640), (200, 640)], spessore=2.6, colore=CELESTE)
    f.rettangolo(395, 740, 50, 30, spessore=1.8)
    f.ellisse(160, 640, 40, 40, spessore=2.6)
    f.testo(160, 712, "pompa", 30)
    f.linea([(160, 600), (160, 470)], spessore=2.6, colore=CELESTE)
    f.rettangolo(120, 380, 80, 90, spessore=2.6)
    f.testo(160, 360, "filtro", 30)
    f.linea([(160, 380), (160, 200), (300, 200)], spessore=2.6, colore=CELESTE)
    f.freccia(310, 200, 420, 200, spessore=2.2, colore=CELESTE, punta=16)
    f.linea([(200, 430), (300, 430)], spessore=2.6, colore=CELESTE)
    f.freccia(300, 430, 420, 450, spessore=2.2, colore=CELESTE, punta=16)
    f.freccia(1000, 380, 860, 420, spessore=2.0, colore=CELESTE, punta=16)
    f.linea([(160, 200), (160, 130), (1080, 130), (1080, 380), (1000, 380)], spessore=2, colore=CELESTE)
    etichetta(f, 1100, 740, 445, 755, "pescante con retina", dim=30)
    for x in (480, 560, 680, 780):
        f.freccia(x, 320, x - 10, 560, curva=0.0, spessore=1.2, passate=1, punta=12, colore=CELESTE)
    f.testo(720, 940, "pompa → filtro → canali in pressione → l'olio ricade nella coppa", 32)
    return f.salva_png(USCITA / "olio-circuito.png")


def aria():
    f = Foglio(1440, 900, seme=93)
    f.testo(720, 70, "raffreddamento ad aria", 56)
    cx = 560
    # cilindro alettato
    for i in range(10):
        y = 200 + i * 42
        w = 260 if i > 1 else 220
        f.linea([(cx - w, y), (cx + w, y)], spessore=3)
        f.linea([(cx - w, y), (cx - w, y + 14), (cx - 120, y + 14)], spessore=1.6, passate=1)
        f.linea([(cx + w, y), (cx + w, y + 14), (cx + 120, y + 14)], spessore=1.6, passate=1)
    f.linea([(cx - 120, 180), (cx - 120, 640)], spessore=3)
    f.linea([(cx + 120, 180), (cx + 120, 640)], spessore=3)
    f.rettangolo(cx - 100, 470, 200, 110, spessore=2.6)
    f.testo(cx, 535, "pistone", 30)
    # aria
    for y in (260, 360, 460):
        f.freccia(60, y, 250, y, spessore=2.6, colore=CELESTE)
        f.freccia(870, y, 1060, y - 20, spessore=2.2, colore=CELESTE)
    f.testo(150, 220, "aria", 40)
    f.testo(1060, 500, "aria calda", 32)
    etichetta(f, 960, 180, cx + 262, 200, "alette: più superficie per cedere calore")
    # radiatore olio
    f.rettangolo(980, 620, 260, 130, spessore=2.8)
    for k in range(1, 9):
        f.linea([(980 + k * 29, 625), (980 + k * 29, 745)], spessore=1.2, passate=1)
    f.testo(1110, 790, "radiatore dell'olio", 32)
    f.linea([(cx + 120, 680), (980, 680)], spessore=2.2, colore=CELESTE)
    f.linea([(cx + 120, 720), (980, 720)], spessore=2.2, colore=CELESTE)
    f.testo(820, 660, "olio", 30)
    f.testo(560, 830, "molti motori \"ad aria\" usano anche l'olio per portare via calore", 32)
    return f.salva_png(USCITA / "raffreddamento-aria.png")


def liquido():
    f = Foglio(1440, 960, seme=95)
    f.testo(720, 70, "raffreddamento a liquido", 56)
    # motore con camicie
    f.rettangolo(160, 300, 360, 380, spessore=3.2)
    f.rettangolo(250, 340, 180, 300, spessore=2.4)
    f.tratteggio(164, 304, 82, 372, passo=12, colore=CELESTE, spessore=1.2)
    f.tratteggio(434, 304, 82, 372, passo=12, colore=CELESTE, spessore=1.2)
    f.testo(340, 720, "motore: il liquido gira", 30)
    f.testo(340, 752, "intorno a cilindro e testata", 30)
    # radiatore
    f.rettangolo(1000, 220, 220, 480, spessore=3.2)
    for k in range(1, 16):
        f.linea([(1004, 220 + k * 30), (1216, 220 + k * 30)], spessore=1.2, passate=1)
    f.testo(1110, 200, "radiatore", 34)
    f.ellisse(1300, 460, 60, 60, spessore=2.6)
    for a in range(0, 360, 90):
        import math
        r = math.radians(a)
        f.linea([(1300, 460), (1300 + 50 * math.cos(r), 460 + 50 * math.sin(r))], spessore=2)
    f.testo(1300, 560, "ventola", 30)
    # termostato
    f.rettangolo(640, 260, 90, 70, spessore=2.6)
    f.testo(685, 240, "termostato", 30)
    # tubi
    f.linea([(520, 300), (640, 295)], spessore=2.6, colore=CELESTE)
    f.freccia(730, 295, 990, 260, spessore=2.6, colore=CELESTE)
    f.testo(860, 245, "caldo", 30)
    f.linea([(1000, 660), (780, 660)], spessore=2.6, colore=CELESTE)
    f.ellisse(730, 660, 50, 50, spessore=2.6)
    f.testo(730, 750, "pompa", 30)
    f.freccia(680, 660, 530, 640, spessore=2.6, colore=CELESTE)
    f.testo(860, 640, "raffreddato", 30)
    # bypass a freddo
    f.linea([(685, 330), (685, 520), (560, 560)], spessore=1.6, passate=1, colore=CELESTE)
    f.testo(710, 450, "a freddo: il termostato", 28, ancora="start")
    f.testo(710, 484, "chiude la via del radiatore", 28, ancora="start")
    # vaso espansione
    f.rettangolo(1040, 760, 140, 90, spessore=2.4)
    f.linea([(1110, 760), (1110, 700)], spessore=1.6)
    f.testo(1110, 890, "vaso di espansione", 30)
    f.testo(720, 940, "pompa → motore → termostato → radiatore → pompa", 30)
    return f.salva_png(USCITA / "raffreddamento-liquido.png")


if __name__ == "__main__":
    for fn in (olio, aria, liquido):
        print(fn())

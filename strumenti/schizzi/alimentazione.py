"""Schizzi del gruppo Alimentazione. Avvio: python3 strumenti/schizzi/alimentazione.py"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, GRAFITE, RADICE, Foglio  # noqa: E402
from manovellismo import etichetta  # noqa: E402

USCITA = RADICE / "public/img/motore"


def farfalla(f, cx, cy, r, ang=35, **kw):
    """Tubo visto in sezione con il disco della farfalla inclinato."""
    a = math.radians(ang)
    dx, dy = r * 0.95 * math.cos(a), r * 0.95 * math.sin(a)
    f.linea([(cx - dx, cy + dy), (cx + dx, cy - dy)], spessore=4, **kw)
    f.ellisse(cx, cy, 7, 7, spessore=2, passate=1)


def carburatore():
    f = Foglio(1440, 1000, seme=71)
    f.testo(720, 70, "il carburatore a saracinesca, in sezione", 54)
    # condotto con venturi
    top = [(120, 300), (480, 300), (600, 360), (760, 360), (880, 300), (1220, 300)]
    bot = [(120, 520), (480, 520), (600, 470), (760, 470), (880, 520), (1220, 520)]
    f.linea(top, spessore=3.2)
    f.linea(bot, spessore=3.2)
    # saracinesca
    f.rettangolo(620, 150, 120, 220, spessore=3)
    f.linea([(600, 150), (600, 360)], spessore=2.4)
    f.linea([(760, 150), (760, 360)], spessore=2.4)
    # spillo conico
    f.linea([(672, 370), (680, 560), (688, 370)], spessore=2.2)
    # polverizzatore
    f.rettangolo(664, 470, 32, 160, spessore=2.4)
    # vaschetta
    f.linea([(520, 630), (520, 860), (840, 860), (840, 630)], spessore=3)
    f.linea([(520, 630), (840, 630)], spessore=2)
    f.tratteggio(522, 720, 316, 138, passo=12, colore=CELESTE, spessore=1.3)
    f.linea([(522, 720), (838, 720)], spessore=1.6, passate=1, colore=CELESTE)
    # getto del massimo
    f.rettangolo(668, 630, 24, 60, spessore=2)
    f.linea([(680, 690), (680, 780)], spessore=1.6, passate=1)
    # galleggiante + valvola a spillo
    f.ellisse(780, 735, 44, 26, spessore=2.6)
    f.linea([(780, 709), (780, 650)], spessore=2.2)
    f.linea([(770, 650), (780, 630), (790, 650)], spessore=2)
    f.linea([(780, 630), (780, 580), (900, 580)], spessore=2.2)
    f.testo(915, 592, "benzina dal serbatoio", 30, ancora="start")
    # flusso aria
    for y in (380, 440):
        f.freccia(170, y, 420, y, spessore=2.4, colore=CELESTE)
    f.freccia(900, 410, 1160, 410, spessore=2.6, colore=CELESTE)
    f.testo(290, 280, "aria", 38)
    f.testo(1040, 280, "miscela verso il motore", 34)
    for i in range(7):
        x, y = 680 + (i - 3) * 12, 455 - (i % 3) * 14
        f.ellisse(x, y, 3, 3, spessore=1.4, passate=1, colore=CELESTE)
    etichetta(f, 820, 150, 740, 200, "saracinesca (valvola gas)")
    etichetta(f, 380, 600, 676, 540, "spillo conico", ancora="end")
    etichetta(f, 380, 660, 664, 600, "polverizzatore", ancora="end")
    etichetta(f, 380, 790, 670, 660, "getto del massimo", ancora="end")
    etichetta(f, 960, 760, 824, 735, "galleggiante")
    etichetta(f, 960, 680, 790, 645, "valvola a spillo")
    etichetta(f, 130, 200, 560, 345, "venturi: l'aria accelera, la pressione cala", dim=30)
    f.testo(720, 940, "la depressione nel venturi aspira la benzina · la saracinesca dosa l'aria", 32)
    return f.salva_png(USCITA / "carburatore-sezione.png")


def iniezione():
    f = Foglio(1440, 960, seme=73)
    f.testo(720, 70, "l'iniezione elettronica: chi decide cosa", 54)
    sensori = ["posizione farfalla (TPS)", "pressione aspirazione (MAP)", "temperatura aria",
               "temperatura motore", "giri e posizione albero", "sonda lambda"]
    for i, s in enumerate(sensori):
        y = 180 + i * 90
        f.rettangolo(80, y - 34, 380, 60, spessore=2.2)
        f.testo(270, y + 6, s, 30)
        f.freccia(470, y - 4, 600, 430, curva=0.05, punta=16, spessore=1.6, passate=1)
    f.rettangolo(610, 330, 260, 200, spessore=3.4)
    f.testo(740, 410, "centralina", 44)
    f.testo(740, 460, "(ECU)", 36)
    f.testo(740, 500, "legge le mappe", 28)
    # uscite
    f.freccia(880, 380, 1060, 240, spessore=2.4)
    f.testo(1180, 220, "iniettore:", 34)
    f.testo(1180, 258, "quanto resta aperto", 30)
    f.freccia(880, 480, 1060, 620, spessore=2.4)
    f.testo(1180, 640, "bobina: anticipo", 34)
    # iniettore disegnato
    f.rettangolo(1150, 290, 60, 110, spessore=2.6)
    f.linea([(1165, 400), (1180, 440), (1195, 400)], spessore=2.2)
    for k in range(-2, 3):
        f.linea([(1180, 448), (1180 + k * 22, 520)], spessore=1.4, passate=1, colore=CELESTE)
    # alimentazione benzina
    f.rettangolo(1080, 760, 220, 90, spessore=2.4)
    f.testo(1190, 815, "pompa benzina", 30)
    f.linea([(1190, 760), (1190, 700), (1360, 700), (1360, 370), (1210, 370)], spessore=2, colore=CELESTE)
    f.testo(1395, 540, "in pressione", 28, ruota=-90)
    f.testo(720, 900, "più sensori leggono, più la centralina dosa la benzina con precisione", 32)
    return f.salva_png(USCITA / "iniezione-schema.png")


def corpo_farfallato():
    f = Foglio(1440, 900, seme=75)
    f.testo(720, 70, "comando a cavo e ride-by-wire", 56)
    for k, (cx, nome) in enumerate(((360, "a cavo"), (1080, "ride-by-wire"))):
        f.testo(cx, 150, nome, 46)
        # manopola
        f.rettangolo(cx - 220, 210, 150, 60, spessore=2.8)
        f.testo(cx - 145, 300, "manopola", 30)
        # corpo farfallato
        f.ellisse(cx + 120, 620, 110, 110, giri=1.05, spessore=3)
        farfalla(f, cx + 120, 620, 110)
        f.testo(cx + 120, 780, "farfalla", 32)
        if k == 0:
            f.linea([(cx - 70, 240), (cx + 40, 260), (cx + 60, 400), (cx + 140, 470), (cx + 200, 520)], spessore=2.4)
            f.testo(cx + 120, 360, "cavo", 32, ancora="start")
            f.rettangolo(cx - 40, 590, 50, 60, spessore=2)
            f.testo(cx - 60, 560, "TPS", 30, ancora="end")
            f.linea([(cx - 15, 620), (cx + 10, 620)], spessore=1.6, passate=1)
        else:
            f.ellisse(cx - 50, 240, 18, 18, spessore=2, colore=CELESTE)
            f.testo(cx - 20, 205, "sensore", 28, ancora="start")
            f.rettangolo(cx - 120, 390, 180, 100, spessore=3)
            f.testo(cx - 30, 450, "centralina", 32)
            f.freccia(cx - 50, 260, cx - 50, 380, spessore=1.8, colore=CELESTE)
            f.rettangolo(cx + 200, 410, 90, 70, spessore=2.6)
            f.testo(cx + 245, 400, "motorino", 28)
            f.freccia(cx + 65, 445, cx + 190, 445, spessore=1.8, colore=CELESTE)
            f.linea([(cx + 245, 480), (cx + 200, 540)], spessore=2)
            f.testo(cx - 200, 530, "mappe, riding mode,", 26, ancora="start")
            f.testo(cx - 200, 562, "controllo di trazione", 26, ancora="start")
    f.linea([(720, 130), (720, 820)], spessore=1.2, passate=1)
    f.testo(720, 860, "nel ride-by-wire la manopola manda un segnale: la farfalla la muove la centralina", 30)
    return f.salva_png(USCITA / "corpo-farfallato.png")


def airbox():
    f = Foglio(1440, 900, seme=77)
    f.testo(720, 70, "airbox e filtro aria", 56)
    # scatola
    f.linea([(260, 220), (1180, 220), (1180, 700), (260, 700), (260, 220)], spessore=3.4)
    # presa d'aria
    f.linea([(80, 380), (260, 400)], spessore=3)
    f.linea([(80, 520), (260, 500)], spessore=3)
    f.freccia(40, 450, 300, 450, spessore=2.6, colore=CELESTE)
    f.testo(150, 340, "presa d'aria", 32)
    # filtro pieghettato
    pts = []
    for i in range(23):
        pts.append((560 + (30 if i % 2 else 0), 240 + i * 20))
    f.linea(pts, spessore=2.6)
    f.linea([(545, 240), (545, 680)], spessore=1.6, passate=1)
    f.linea([(605, 240), (605, 680)], spessore=1.6, passate=1)
    f.testo(410, 650, "lato sporco", 32)
    f.testo(760, 650, "lato pulito", 32)
    # polvere bloccata
    for (x, y) in ((500, 300), (520, 380), (490, 470), (530, 560), (505, 420)):
        f.ellisse(x, y, 4, 4, spessore=1.6, passate=1)
    # cornetti + corpi farfallati
    for i, y in enumerate((330, 560)):
        f.linea([(960, y - 50), (1010, y - 30), (1180, y - 30)], spessore=2.8)
        f.linea([(960, y + 50), (1010, y + 30), (1180, y + 30)], spessore=2.8)
        f.linea([(1180, y - 30), (1300, y - 30)], spessore=2.8)
        f.linea([(1180, y + 30), (1300, y + 30)], spessore=2.8)
        f.freccia(700, y, 940, y, spessore=2.2, colore=CELESTE)
        f.freccia(1200, y, 1320, y, spessore=2.2, colore=CELESTE)
    f.testo(1060, 460, "cornetti", 32)
    f.testo(1330, 460, "verso", 30)
    f.testo(1330, 495, "il motore", 30)
    etichetta(f, 760, 160, 590, 240, "filtro: trattiene polvere e sporco")
    f.testo(720, 800, "volume calmo d'aria pulita · meno rumore di aspirazione · aria uniforme sul filtro", 30)
    return f.salva_png(USCITA / "airbox-filtro.png")


if __name__ == "__main__":
    for fn in (carburatore, iniezione, corpo_farfallato, airbox):
        print(fn())

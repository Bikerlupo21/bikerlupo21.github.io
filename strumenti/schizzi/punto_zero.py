"""Schizzi dell'articolo "Punto zero". Avvio: python3 strumenti/schizzi/punto_zero.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, GRAFITE, RADICE, Foglio  # noqa: E402

USCITA = RADICE / "public/img/articoli/punto-zero"


def sportiva(f, cx, cy, s=1.0, colore=GRAFITE):
    """Moto sportiva carenata vista di lato (generica, ispirata a una 600 supersport). cy = asse ruote."""
    p = lambda x, y: (cx + x * s, cy + y * s)  # noqa: E731
    r = 62
    # ruote e dischi
    for wx in (-190, 190):
        f.ellisse(*p(wx, 0), r * s, r * s, spessore=3.2, colore=colore)
        f.ellisse(*p(wx, 0), 44 * s, 44 * s, spessore=1.4, passate=1, colore=colore)
        f.ellisse(*p(wx, 0), 9 * s, 9 * s, spessore=2, passate=1, colore=colore)
    # forcella
    f.linea([p(190, 0), p(135, -150)], spessore=3.4, colore=colore)
    f.linea([p(176, 4), p(121, -146)], spessore=2, passate=1, colore=colore)
    # forcellone
    f.linea([p(-190, 0), p(-20, -40)], spessore=3.2, colore=colore)
    f.linea([p(-190, -10), p(-20, -52)], spessore=1.6, passate=1, colore=colore)
    # carena laterale + puntale
    f.linea([p(140, -160), p(185, -120), p(170, -70), p(110, -30), p(30, -12), p(-30, -28),
             p(-10, -90), p(60, -150), p(140, -160)], spessore=3, colore=colore)
    # cupolino e plexi
    f.linea([p(140, -160), p(120, -205), p(80, -215), p(60, -150)], spessore=2.8, colore=colore)
    # serbatoio e sella
    f.linea([p(80, -215), p(30, -205), p(-30, -185), p(-90, -175), p(-140, -190), p(-215, -205)], spessore=3, colore=colore)
    f.linea([p(-215, -205), p(-230, -180), p(-150, -150), p(-60, -120), p(-10, -90)], spessore=2.8, colore=colore)
    # codino alto
    f.linea([p(-140, -190), p(-225, -232), p(-245, -225), p(-215, -205)], spessore=2.6, colore=colore)
    # scarico sotto il codino
    f.linea([p(-60, -120), p(-170, -150), p(-205, -140)], spessore=2.2, passate=1, colore=colore)
    # dettagli carena (prese d'aria)
    f.linea([p(120, -110), p(70, -80), p(30, -70)], spessore=1.6, passate=1, colore=colore)
    f.tratteggio(*p(60, -140), 60 * s, 40 * s, passo=12, spessore=1.2, colore=colore)
    # manubrio
    f.linea([p(95, -205), p(70, -195), p(50, -200)], spessore=2.4, colore=colore)


def copertina():
    f = Foglio(1600, 900, seme=1114)
    f.testo(800, 130, "punto zero", 120)
    f.testo(800, 205, "Bikerlupo riparte da zero", 48)
    f.linea([(330, 720), (1270, 720)], spessore=2.4)
    sportiva(f, 800, 655, s=1.25, colore=GRAFITE)
    f.testo(1130, 330, "Selly", 64, colore=CELESTE)
    f.freccia(1100, 350, 1000, 420, spessore=2.6, colore=CELESTE)
    f.testo(800, 800, "CBR 600 RR del 2010 · stesso nome, stesso canale", 40)
    f.scintilla(250, 160, r=34, spessore=2)
    f.scintilla(1360, 120, r=26, spessore=2, colore=CELESTE)
    return f.salva_png(USCITA / "copertina.png")


def logo():
    f = Foglio(1440, 760, seme=2110)
    f.testo(720, 80, "cosa vuol dire BL21", 58)
    f.testo(460, 320, "BL", 200)
    f.testo(900, 320, "21", 200, colore=CELESTE)
    f.freccia(440, 360, 380, 470, spessore=2.6)
    f.testo(330, 530, "Bikerlupo", 50)
    f.testo(330, 575, "resta Bikerlupo", 34)
    f.freccia(900, 360, 920, 470, spessore=2.6, colore=CELESTE)
    f.testo(960, 530, "21 ottobre", 50)
    f.testo(960, 575, "è nata mia figlia", 34)
    f.ellisse(1230, 290, 120, 70, spessore=2.4, colore=CELESTE)
    f.testo(1230, 285, "celeste", 44, colore=CELESTE)
    f.testo(1230, 325, "come lei: Celeste", 26)
    f.testo(720, 690, "una vena un pochino più romantica", 40)
    return f.salva_png(USCITA / "logo-bl21.png")


def obiettivi():
    f = Foglio(1440, 720, seme=2027)
    f.testo(720, 80, "gli obiettivi", 58)
    # sinistra: la moto finita a EICMA
    sportiva(f, 380, 420, s=0.75, colore=CELESTE)
    f.linea([(170, 470), (590, 470)], spessore=2)
    f.testo(380, 560, "EICMA 2027", 60)
    f.testo(380, 610, "con la moto finita", 34)
    # destra: iscritti
    f.rettangolo(870, 200, 380, 230, spessore=2.6)
    f.linea([(1020, 270), (1020, 360), (1110, 315), (1020, 270)], spessore=2.6, colore=CELESTE)
    f.testo(1060, 560, "20.000 iscritti", 60)
    f.testo(1060, 610, "ambizioso, ma sfidante", 34)
    f.freccia(700, 300, 820, 300, spessore=2.4)
    return f.salva_png(USCITA / "obiettivi.png")


if __name__ == "__main__":
    USCITA.mkdir(parents=True, exist_ok=True)
    for fn in (copertina, logo, obiettivi):
        print(fn())

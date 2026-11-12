"""Schizzi del gruppo Manovellismo. Avvio: python3 strumenti/schizzi/manovellismo.py"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, RADICE, Foglio  # noqa: E402

USCITA = RADICE / "public/img/motore"


def etichetta(f, xt, yt, xp, yp, testo, ancora="start", dim=34):
    f.testo(xt, yt, testo, dim, ancora=ancora, ruota=0)
    xa = xt - 10 if ancora == "start" else xt + 10
    f.linea([(xa, yt - 10), (xp, yp)], spessore=1.6, passate=1, ampiezza=0.6)
    f.ellisse(xp, yp, 5, 5, spessore=1.6, passate=1)


def pistone():
    f = Foglio(1440, 900, seme=51)
    f.testo(720, 70, "il pistone e le fasce elastiche", 56)
    x0, x1, top = 420, 860, 180
    # cielo
    f.linea([(x0, top + 30), (x0 + 40, top), (x1 - 40, top), (x1, top + 30)], spessore=3.6)
    f.linea([(x0, top + 30), (x0, 720)], spessore=3.4)
    f.linea([(x1, top + 30), (x1, 720)], spessore=3.4)
    f.linea([(x0, 720), (x1, 720)], spessore=2.4, passate=1)
    # cave delle fasce
    for k, y in enumerate((top + 60, top + 100, top + 145)):
        h = 14 if k < 2 else 24
        f.rettangolo(x0 - 6, y, 40, h, spessore=2)
        f.rettangolo(x1 - 34, y, 40, h, spessore=2)
        f.linea([(x0 + 40, y + h / 2), (x1 - 40, y + h / 2)], spessore=1.4, passate=1)
    f.tratteggio(x0 - 4, top + 62, 36, 10, passo=5, colore=CELESTE, spessore=1.6)
    f.tratteggio(x1 - 32, top + 62, 36, 10, passo=5, colore=CELESTE, spessore=1.6)
    # portate e spinotto
    cx = (x0 + x1) / 2
    f.ellisse(cx, 470, 70, 70, spessore=3)
    f.ellisse(cx, 470, 38, 38, spessore=2.4)
    f.linea([(x0 + 30, 400), (cx - 70, 430)], spessore=2.4)
    f.linea([(x1 - 30, 400), (cx + 70, 430)], spessore=2.4)
    # etichette
    etichetta(f, 960, 190, x1 - 60, top + 4, "cielo (a contatto con i gas)")
    etichetta(f, 960, 250, x1 + 4, top + 67, "1ª fascia: tenuta")
    etichetta(f, 960, 310, x1 + 4, top + 107, "2ª fascia: tenuta e olio")
    etichetta(f, 960, 370, x1 + 4, top + 157, "raschiaolio")
    etichetta(f, 960, 470, cx + 38, 470, "spinotto (va alla biella)")
    etichetta(f, 960, 620, x1, 640, "mantello: guida nel cilindro")
    f.testo(250, 470, "portate", 34)
    f.linea([(290, 456), (cx - 70, 470)], spessore=1.6, passate=1)
    f.testo(720, 820, "le fasce portano anche il calore dal pistone al cilindro", 32)
    return f.salva_png(USCITA / "pistone-fasce.png")


def biella():
    f = Foglio(1440, 900, seme=53)
    f.testo(720, 70, "la biella", 58)
    cx, yp, yt = 560, 210, 640
    # piede (lato pistone)
    f.ellisse(cx, yp, 62, 62, spessore=3.2)
    f.ellisse(cx, yp, 34, 34, spessore=2.4)
    # fusto con sezione ad H (due linee + nervatura)
    f.linea([(cx - 34, yp + 58), (cx - 70, yt - 120)], spessore=3)
    f.linea([(cx + 34, yp + 58), (cx + 70, yt - 120)], spessore=3)
    f.linea([(cx, yp + 70), (cx, yt - 140)], spessore=1.6, passate=1)
    # testa (lato albero) con cappello e viti
    f.ellisse(cx, yt, 120, 120, spessore=3.4)
    f.ellisse(cx, yt, 80, 80, spessore=2.4)
    f.ellisse(cx, yt, 72, 72, spessore=1.4, passate=1)
    f.linea([(cx - 150, yt), (cx + 150, yt)], spessore=2.6)
    for s in (-1, 1):
        f.rettangolo(cx + s * 100 - 9, yt - 70, 18, 160, spessore=2)
    etichetta(f, 820, 210, cx + 62, yp, "piede: si collega al pistone")
    etichetta(f, 820, 260, cx + 34, yp + 10, "con lo spinotto")
    etichetta(f, 820, 400, cx + 52, 400, "fusto")
    etichetta(f, 820, 560, cx + 78, yt - 20, "testa: si collega all'albero")
    etichetta(f, 820, 620, cx + 72, yt + 10, "bronzina (cuscinetto)")
    etichetta(f, 820, 700, cx + 60, yt + 90, "cappello")
    etichetta(f, 820, 760, cx + 109, yt + 70, "viti del cappello")
    f.testo(720, 850, "testa scomponibile: tipica dei pluricilindrici con albero in un pezzo", 30)
    return f.salva_png(USCITA / "biella.png")


def albero():
    f = Foglio(1440, 820, seme=55)
    f.testo(720, 70, "l'albero motore di un monocilindrico", 54)
    y = 430
    # perni di banco
    f.rettangolo(170, y - 35, 230, 70, spessore=3)
    f.rettangolo(1040, y - 35, 230, 70, spessore=3)
    # volantini/bracci
    for x in (400, 920):
        f.linea([(x, y - 230), (x, y + 230)], spessore=3.2)
        f.linea([(x + 120, y - 230), (x + 120, y + 230)], spessore=3.2)
        f.linea([(x, y - 230), (x + 120, y - 230)], spessore=3)
        f.linea([(x, y + 230), (x + 120, y + 230)], spessore=3)
        f.tratteggio(x + 4, y + 60, 112, 166, passo=10, spessore=1.6)
    # perno di manovella (eccentrico, in alto)
    yp = y - 140
    f.rettangolo(520, yp - 35, 400, 70, spessore=3)
    f.linea([(150, y), (1290, y)], spessore=1.4, passate=1)
    for xx in range(150, 1290, 40):
        pass
    f.linea([(520, yp), (920, yp)], spessore=1.2, passate=1)
    # raggio di manovella
    f.freccia(720, y, 720, yp + 4, curva=0, punta=14, spessore=2.4)
    f.testo(700, y - 50, "raggio di manovella", 32, ancora="end")
    f.testo(700, y - 14, "= metà della corsa", 32, ancora="end")
    etichetta(f, 220, 620, 285, y + 35, "perno di banco", ancora="start")
    etichetta(f, 1080, 620, 1155, y + 35, "perno di banco")
    etichetta(f, 560, 170, 650, yp - 35, "perno di manovella (qui lavora la biella)")
    etichetta(f, 220, 760, 460, y + 160, "contrappeso: bilancia le masse in movimento")
    f.testo(1160, 780, "asse di rotazione", 30)
    f.linea([(1160, 750), (1180, y + 8)], spessore=1.4, passate=1)
    return f.salva_png(USCITA / "albero-motore.png")


def cilindro_testata():
    f = Foglio(1440, 900, seme=57)
    f.testo(720, 70, "cilindro e testata", 58)
    xl, xr = 470, 790
    # testata
    f.linea([(xl - 70, 280), (xl - 70, 170), (xr + 70, 170), (xr + 70, 280)], spessore=3.4)
    f.linea([(xl - 70, 280), (xl + 30, 280), (xl + 80, 250), (xr - 80, 250), (xr - 30, 280), (xr + 70, 280)], spessore=3)
    for s in (-1, 1):
        xv = (xl + xr) / 2 + s * 70
        f.linea([(xv, 120), (xv + s * 20, 245)], spessore=2.6)
        f.linea([(xv + s * 20 - 28, 250), (xv + s * 20 + 28, 250)], spessore=3)
    f.linea([((xl + xr) / 2, 130), ((xl + xr) / 2, 250)], spessore=2.4)
    # guarnizione
    f.linea([(xl - 70, 292), (xr + 70, 292)], spessore=5, colore=CELESTE)
    # cilindro con riporto
    f.linea([(xl, 300), (xl, 720)], spessore=3.4)
    f.linea([(xr, 300), (xr, 720)], spessore=3.4)
    f.linea([(xl + 8, 300), (xl + 8, 720)], spessore=1.4, passate=1)
    f.linea([(xr - 8, 300), (xr - 8, 720)], spessore=1.4, passate=1)
    for y in range(320, 700, 30):
        f.linea([(xl - 90, y), (xl, y)], spessore=2, passate=1)
        f.linea([(xr, y), (xr + 90, y)], spessore=2, passate=1)
    f.rettangolo(xl + 14, 420, xr - xl - 28, 110, spessore=2.6)
    etichetta(f, 960, 140, xr - 60, 175, "testata")
    etichetta(f, 960, 200, (xl + xr) / 2 + 2, 200, "candela")
    etichetta(f, 960, 250, (xl + xr) / 2 + 90, 250, "valvole")
    etichetta(f, 960, 300, xr - 40, 268, "camera di combustione")
    etichetta(f, 960, 360, xr + 60, 292, "guarnizione di testa")
    etichetta(f, 960, 470, xr - 8, 470, "canna (dove scorre il pistone)")
    etichetta(f, 960, 560, xr + 80, 560, "alette (raffreddamento ad aria)")
    f.testo(720, 830, "schema semplificato · nei motori a liquido al posto delle alette ci sono i passaggi dell'acqua", 30)
    return f.salva_png(USCITA / "cilindro-testata.png")


if __name__ == "__main__":
    for fn in (pistone, biella, albero, cilindro_testata):
        print(fn())

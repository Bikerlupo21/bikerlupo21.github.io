"""Schizzi del gruppo Trasmissione. Avvio: python3 strumenti/schizzi/trasmissione.py"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, GRAFITE, RADICE, Foglio  # noqa: E402
from manovellismo import etichetta  # noqa: E402

USCITA = RADICE / "public/img/motore"


def ruota_dentata(f, cx, cy, r, denti, **kw):
    pts = []
    n = denti * 4
    for i in range(n + 1):
        a = i / n * math.tau
        rr = r if (i % 4) in (0, 1) else r - 10
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    f.linea(pts, **kw)


def frizione():
    f = Foglio(1440, 980, seme=101)
    f.testo(720, 70, "la frizione multidisco, in sezione", 56)
    x0, x1 = 360, 760
    # campana (esterna)
    f.linea([(x0 - 40, 180), (x0 - 40, 760), (x1 + 20, 760)], spessore=3.4)
    f.linea([(x0 - 40, 180), (x1 + 20, 180)], spessore=3.4)
    # mozzo (interno)
    f.rettangolo(x0, 440, x1 - x0 + 120, 80, spessore=2.8)
    f.linea([(x1 + 120, 480), (1000, 480)], spessore=3)
    # dischi alternati
    for i in range(9):
        x = x0 + 20 + i * 40
        if i % 2 == 0:  # guarnito, preso dalla campana (esterno)
            f.linea([(x, 190), (x, 420)], spessore=6, colore=CELESTE)
            f.linea([(x, 540), (x, 750)], spessore=6, colore=CELESTE)
        else:  # metallico, preso dal mozzo (interno)
            f.linea([(x, 230), (x, 440)], spessore=3)
            f.linea([(x, 520), (x, 720)], spessore=3)
    # spingidisco e molle
    xs = x0 + 20 + 9 * 40
    f.linea([(xs, 210), (xs, 440)], spessore=4)
    f.linea([(xs, 520), (xs, 740)], spessore=4)
    for y in (300, 660):
        pts = [(xs + 10 + t * 4, y + 18 * math.sin(t * 1.2)) for t in range(0, 40)]
        f.linea(pts, spessore=2, passate=1)
    # leva / astina
    f.freccia(1180, 480, 1010, 480, spessore=2.6)
    f.testo(1180, 440, "tiri la leva:", 30, ancora="start")
    f.testo(1180, 476, "lo spingidisco si stacca", 28, ancora="start")
    f.testo(1180, 508, "e i dischi si separano", 28, ancora="start")
    etichetta(f, 60, 140, x0 - 36, 230, "campana: la fa girare il motore", ancora="start")
    etichetta(f, 900, 160, x0 + 100, 200, "dischi guarniti (prendono la campana)")
    etichetta(f, 900, 810, x0 + 140, 700, "dischi metallici (prendono il mozzo)")
    etichetta(f, 900, 620, xs + 60, 660, "molle: tengono il pacco premuto")
    etichetta(f, 120, 860, x0 + 60, 515, "mozzo → cambio", ancora="start")
    f.testo(720, 930, "leva rilasciata: le molle stringono il pacco e il moto passa al cambio", 30)
    return f.salva_png(USCITA / "frizione-sezione.png")


def cambio():
    f = Foglio(1440, 1000, seme=103)
    f.testo(720, 70, "il cambio a ingranaggi sempre in presa", 54)
    ya, yb = 300, 560  # primario, secondario
    f.linea([(140, ya), (1100, ya)], spessore=3)
    f.linea([(140, yb), (1100, yb)], spessore=3)
    f.testo(120, ya + 10, "primario", 30, ancora="end")
    f.testo(120, yb + 10, "secondario", 30, ancora="end")
    coppie = [(260, 70, 150), (420, 95, 125), (580, 115, 105), (740, 130, 90)]
    for k, (x, ra, rb) in enumerate(coppie):
        f.rettangolo(x - 22, ya - ra, 44, 2 * ra, spessore=2.6)
        f.rettangolo(x - 22, yb - rb, 44, 2 * rb, spessore=2.6)
        f.testo(x, ya - ra - 18, f"{k + 1}ª", 34)
    # ingranaggio scorrevole con innesti frontali sul secondario
    xs = 500
    f.rettangolo(xs - 16, yb - 60, 32, 120, spessore=3.2, colore=CELESTE)
    for dy in (-40, 0, 40):
        f.linea([(xs + 16, yb + dy - 8), (xs + 34, yb + dy - 8), (xs + 34, yb + dy + 8), (xs + 16, yb + dy + 8)], spessore=2, colore=CELESTE)
    # forcella
    f.linea([(xs, yb + 60), (xs, 720), (xs + 20, 740)], spessore=3)
    # tamburo selettore
    f.rettangolo(300, 740, 600, 60, spessore=3)
    f.linea([(320, 770), (420, 770), (480, 755), (560, 785), (640, 770), (880, 770)], spessore=2, colore=CELESTE)
    f.ellisse(xs + 20, 770, 8, 8, spessore=2, passate=1)
    etichetta(f, 960, 640, xs + 30, yb + 40, "innesti frontali (\"dogs\")")
    etichetta(f, 960, 700, xs + 6, 700, "forcella")
    etichetta(f, 960, 770, 900, 770, "tamburo selettore con le cave")
    etichetta(f, 960, 200, 760, ya - 120, "ingranaggi sempre in presa, a coppie")
    f.freccia(1240, 300, 1120, 300, spessore=2.2, colore=CELESTE)
    f.testo(1250, 310, "dalla frizione", 28, ancora="start")
    f.freccia(1120, 560, 1240, 560, spessore=2.2, colore=CELESTE)
    f.testo(1250, 570, "al pignone", 28, ancora="start")
    f.testo(720, 900, "il pedale ruota il tamburo · le cave muovono le forcelle · i denti frontali agganciano la marcia", 28)
    return f.salva_png(USCITA / "cambio-sequenziale.png")


def finale():
    f = Foglio(1440, 900, seme=105)
    f.testo(720, 70, "catena, cinghia e cardano", 56)
    # catena
    cx = 240
    ruota_dentata(f, cx - 110, 330, 40, 14, spessore=2.4)
    ruota_dentata(f, cx + 90, 330, 110, 40, spessore=2.4)
    f.linea([(cx - 110, 290), (cx + 90, 220)], spessore=2.6, colore=CELESTE)
    f.linea([(cx - 110, 370), (cx + 90, 440)], spessore=2.6, colore=CELESTE)
    f.testo(cx - 110, 410, "pignone", 28)
    f.testo(cx + 90, 480, "corona", 28)
    f.testo(cx, 560, "catena", 42)
    f.testo(cx, 610, "leggera, rapporti facili", 26)
    f.testo(cx, 642, "da cambiare", 26)
    f.testo(cx, 690, "va pulita, oliata", 26)
    f.testo(cx, 722, "e tesa spesso", 26)
    # cinghia
    cx = 720
    f.ellisse(cx - 110, 330, 55, 55, spessore=2.6)
    f.ellisse(cx + 90, 330, 115, 115, spessore=2.6)
    f.linea([(cx - 110, 275), (cx + 90, 215)], spessore=7, passate=1, colore=CELESTE)
    f.linea([(cx - 110, 385), (cx + 90, 445)], spessore=7, passate=1, colore=CELESTE)
    f.testo(cx, 560, "cinghia dentata", 42)
    f.testo(cx, 610, "silenziosa, niente olio", 26)
    f.testo(cx, 642, "dura a lungo", 26)
    f.testo(cx, 690, "più ingombrante,", 26)
    f.testo(cx, 722, "costosa da sostituire", 26)
    # cardano
    cx = 1180
    f.rettangolo(cx - 200, 300, 70, 70, spessore=2.6)
    f.testo(cx - 165, 280, "cambio", 26)
    f.linea([(cx - 130, 325), (cx + 40, 325)], spessore=3)
    f.linea([(cx - 130, 345), (cx + 40, 345)], spessore=3)
    f.ellisse(cx - 60, 335, 14, 22, spessore=2, passate=1)
    f.rettangolo(cx + 40, 290, 80, 90, spessore=3)
    f.ellisse(cx + 160, 335, 30, 100, spessore=2.6)
    f.testo(cx + 80, 420, "coppia conica", 26)
    f.testo(cx + 160, 460, "ruota", 26)
    f.testo(cx, 560, "cardano", 42)
    f.testo(cx, 610, "chiuso e in olio,", 26)
    f.testo(cx, 642, "manutenzione minima", 26)
    f.testo(cx, 690, "più pesante,", 26)
    f.testo(cx, 722, "rapporti difficili da cambiare", 26)
    f.linea([(480, 160), (480, 760)], spessore=1.2, passate=1)
    f.linea([(960, 160), (960, 760)], spessore=1.2, passate=1)
    f.testo(720, 830, "tre modi per portare il moto dal cambio alla ruota posteriore", 32)
    return f.salva_png(USCITA / "trasmissione-finale.png")


if __name__ == "__main__":
    for fn in (frizione, cambio, finale):
        print(fn())

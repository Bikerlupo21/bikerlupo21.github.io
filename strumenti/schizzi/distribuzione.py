"""Schizzi del gruppo Distribuzione. Avvio: python3 strumenti/schizzi/distribuzione.py"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, GRAFITE, RADICE, Foglio  # noqa: E402
from manovellismo import etichetta  # noqa: E402

USCITA = RADICE / "public/img/motore"


def camma(f, cx, cy, r, alzata, rot=0, **kw):
    """Profilo di camma: cerchio di base + lobo."""
    pts = []
    for i in range(73):
        a = math.radians(i * 5)
        d = math.cos(a - math.radians(rot))
        extra = alzata * max(0, d) ** 3
        pts.append((cx + (r + extra) * math.cos(a), cy + (r + extra) * math.sin(a)))
    f.linea(pts, **kw)


def valvola():
    f = Foglio(1440, 980, seme=61)
    f.testo(1040, 80, "la valvola e il suo comando", 54)
    cx = 560
    camma(f, cx, 180, 56, 50, rot=-90, spessore=3)
    f.ellisse(cx, 180, 10, 10, spessore=2, passate=1)
    # punteria a bicchiere
    f.rettangolo(cx - 60, 250, 120, 70, spessore=3)
    # gioco
    f.linea([(cx - 70, 240), (cx + 70, 240)], spessore=1.2, passate=1, colore=CELESTE)
    # molla
    pts = []
    for i in range(0, 121):
        t = i / 120
        pts.append((cx + 52 * math.sin(t * math.tau * 6), 330 + t * 210))
    f.linea(pts, spessore=2.2, passate=1)
    f.rettangolo(cx - 64, 322, 128, 14, spessore=2.4)  # scodellino
    # stelo e guida
    f.linea([(cx - 9, 320), (cx - 9, 770)], spessore=2.6)
    f.linea([(cx + 9, 320), (cx + 9, 770)], spessore=2.6)
    f.rettangolo(cx - 22, 560, 44, 150, spessore=2.4)
    # testata e sede
    f.linea([(250, 545), (cx - 70, 545)], spessore=3)
    f.linea([(cx + 70, 545), (900, 545)], spessore=3)
    f.linea([(250, 790), (cx - 90, 790), (cx - 70, 770)], spessore=3)
    f.linea([(900, 790), (cx + 90, 790), (cx + 70, 770)], spessore=3)
    # fungo (chiuso sulla sede)
    f.linea([(cx - 9, 760), (cx - 72, 785), (cx - 80, 798), (cx + 80, 798), (cx + 72, 785), (cx + 9, 760)], spessore=3.4)
    f.tratteggio(cx - 78, 784, 156, 12, passo=6, colore=CELESTE, spessore=1.4)
    etichetta(f, 860, 200, cx + 60, 190, "camma (sull'albero a camme)")
    etichetta(f, 860, 245, cx + 70, 240, "gioco valvola", )
    etichetta(f, 860, 300, cx + 60, 290, "punteria a bicchiere")
    etichetta(f, 860, 360, cx + 64, 330, "scodellino e semiconi")
    etichetta(f, 860, 440, cx + 52, 440, "molla: richiude la valvola")
    etichetta(f, 860, 630, cx + 22, 630, "guida")
    etichetta(f, 860, 700, cx + 9, 700, "stelo")
    etichetta(f, 860, 790, cx + 76, 790, "fungo appoggiato sulla sede")
    f.testo(720, 920, "la camma apre spingendo verso il basso · la molla richiude", 34)
    return f.salva_png(USCITA / "valvola.png")


def alberi():
    f = Foglio(1440, 820, seme=63)
    f.testo(720, 70, "monoalbero e bialbero", 58)
    for k, (cx, nome) in enumerate(((360, "monoalbero (un albero a camme)"), (1080, "bialbero (due alberi a camme)"))):
        y = 520
        f.linea([(cx - 230, y), (cx + 230, y)], spessore=3)
        f.linea([(cx - 230, y), (cx - 230, y - 200), (cx + 230, y - 200), (cx + 230, y)], spessore=3)
        for s in (-1, 1):
            xv = cx + s * 90
            f.linea([(xv, y + 30), (xv + s * 30, y - 140)], spessore=2.6)
            f.linea([(xv - 30, y + 30), (xv + 30, y + 30)], spessore=3)
        if k == 0:
            camma(f, cx, y - 260, 40, 34, rot=-90, spessore=3)
            for s in (-1, 1):
                f.linea([(cx + s * 40, y - 230), (cx + s * 120, y - 160)], spessore=4)  # bilancieri
            f.testo(cx + 140, y - 290, "bilancieri", 32, ancora="start")
        else:
            for s in (-1, 1):
                camma(f, cx + s * 120, y - 230, 36, 30, rot=90, spessore=3)
            f.testo(cx, y - 300, "aspirazione · scarico", 32)
        f.testo(cx, y + 110, nome, 38)
    f.testo(720, 760, "in entrambi i casi l'albero a camme gira a metà dei giri dell'albero motore", 32)
    return f.salva_png(USCITA / "monoalbero-bialbero.png")


def catena():
    f = Foglio(1440, 900, seme=65)
    f.testo(720, 70, "il comando della distribuzione", 56)
    cx, ya, yb = 600, 220, 720
    R, r = 110, 55
    f.ellisse(cx, ya, R, R, spessore=3)
    f.ellisse(cx, yb, r, r, spessore=3)
    for a in range(0, 360, 20):
        x, y = cx + R * math.cos(math.radians(a)), ya + R * math.sin(math.radians(a))
        f.linea([(x, y), (cx + (R + 10) * math.cos(math.radians(a)), ya + (R + 10) * math.sin(math.radians(a)))], spessore=1.6, passate=1)
    for a in range(0, 360, 40):
        f.linea([(cx + r * math.cos(math.radians(a)), yb + r * math.sin(math.radians(a))), (cx + (r + 10) * math.cos(math.radians(a)), yb + (r + 10) * math.sin(math.radians(a)))], spessore=1.6, passate=1)
    # rami della catena
    f.linea([(cx - R - 8, ya), (cx - r - 8, yb)], spessore=3, colore=CELESTE)
    f.linea([(cx + R + 8, ya), (cx + r + 8, yb)], spessore=3, colore=CELESTE)
    # pattino e tendicatena
    f.linea([(cx + R + 22, ya + 60), (cx + r + 30, yb - 80)], spessore=6)
    f.rettangolo(cx + 150, 430, 90, 40, spessore=2.4)
    f.freccia(cx + 150, 450, cx + 108, 450, curva=0, punta=12, spessore=2.2)
    etichetta(f, 900, 200, cx + R, ya - 20, "corona sull'albero a camme")
    etichetta(f, 900, 250, cx + 40, ya + 20, "(il doppio dei denti)")
    etichetta(f, 900, 450, cx + 240, 450, "tendicatena")
    etichetta(f, 900, 540, cx + 120, 520, "pattino")
    etichetta(f, 900, 720, cx + r, yb, "pignone sull'albero motore")
    f.testo(cx - R - 40, (ya + yb) / 2, "catena", 36, ancora="end")
    f.testo(720, 850, "corona con il doppio dei denti = l'albero a camme gira a metà", 34)
    return f.salva_png(USCITA / "catena-distribuzione.png")


def fasatura():
    f = Foglio(1440, 980, seme=67)
    f.testo(720, 70, "il diagramma della distribuzione", 56)
    cx, cy, R = 620, 520, 300
    f.ellisse(cx, cy, R, R, spessore=2, passate=1)
    f.linea([(cx, cy - R - 40), (cx, cy + R + 40)], spessore=1.6, passate=1)
    f.testo(cx, cy - R - 54, "PMS", 40)
    f.testo(cx, cy + R + 82, "PMI", 40)

    def p(ang, rr):
        a = math.radians(ang - 90)
        return cx + rr * math.cos(a), cy + rr * math.sin(a)

    def arco(a0, a1, rr, **kw):
        n = max(6, int(abs(a1 - a0) / 4))
        f.linea([p(a0 + (a1 - a0) * i / n, rr) for i in range(n + 1)], **kw)

    # angoli qualitativi (in gradi dal PMS, senso orario) solo per il disegno
    AA, CA = -25, 180 + 55
    AS, CS = 180 - 55, 360 + 20
    arco(AA, CA, R - 40, spessore=6, colore=CELESTE)
    arco(AS, CS, R - 90, spessore=6, colore=GRAFITE)
    arco(AA, CS - 360, R + 30, spessore=3)
    for ang, rr, t, anc in ((AA, R - 40, "AA", "end"), (CA, R - 40, "CA", "end"), (AS, R - 90, "AS", "start"), (CS, R - 90, "CS", "start")):
        x, y = p(ang, rr)
        f.ellisse(x, y, 7, 7, spessore=2, passate=1)
        tx, ty = p(ang, rr + (70 if t in ("AA", "CS") else 60))
        f.testo(tx, ty + 12, t, 36)
    tx, ty = p(0, R + 70)
    f.testo(tx + 150, ty - 6, "incrocio", 36, ancora="start")
    f.linea([(tx + 140, ty - 18), p(-2, R + 30)], spessore=1.4, passate=1)
    X = 1000
    f.testo(X, 330, "AA apre l'aspirazione: prima del PMS", 32, ancora="start", colore=GRAFITE)
    f.testo(X, 375, "CA chiude l'aspirazione: dopo il PMI", 32, ancora="start")
    f.testo(X, 440, "AS apre lo scarico: prima del PMI", 32, ancora="start")
    f.testo(X, 485, "CS chiude lo scarico: dopo il PMS", 32, ancora="start")
    f.linea([(X, 560), (X + 60, 560)], spessore=6, colore=CELESTE)
    f.testo(X + 80, 572, "aspirazione aperta", 32, ancora="start")
    f.linea([(X, 610), (X + 60, 610)], spessore=6)
    f.testo(X + 80, 622, "scarico aperto", 32, ancora="start")
    f.testo(720, 940, "schema qualitativo · i gradi veri cambiano da motore a motore", 32)
    return f.salva_png(USCITA / "fasatura-diagramma.png")


if __name__ == "__main__":
    for fn in (valvola, alberi, catena, fasatura):
        print(fn())

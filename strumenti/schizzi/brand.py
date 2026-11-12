"""Schizzi delle schede brand. Avvio: python3 strumenti/schizzi/brand.py"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, GRAFITE, RADICE, Foglio  # noqa: E402
from manovellismo import etichetta  # noqa: E402

USCITA = RADICE / "public/img/brand"


def liscia(pts, giri=3):
    """Arrotonda una spezzata chiusa (Chaikin)."""
    for _ in range(giri):
        nuovi = []
        for i in range(len(pts)):
            (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % len(pts)]
            nuovi += [(0.75 * x1 + 0.25 * x2, 0.75 * y1 + 0.25 * y2), (0.25 * x1 + 0.75 * x2, 0.25 * y1 + 0.75 * y2)]
        pts = nuovi
    return pts


def casco_profilo(f, cx, cy, s=1.0, **kw):
    """Casco integrale visto di lato, rivolto a destra."""
    base = [(-150, 115), (-178, 10), (-130, -115), (0, -165), (125, -115), (172, -15), (178, 75), (125, 125), (-40, 128)]
    f.linea(liscia([(cx + x * s, cy + y * s) for x, y in base]), chiuso=True, spessore=3.2, **kw)
    vis = [(15, -75), (145, -70), (168, 0), (40, 18)]
    f.linea(liscia([(cx + x * s, cy + y * s) for x, y in vis], 2), chiuso=True, spessore=2.6)
    f.tratteggio(cx + 40 * s, cy - 60 * s, 110 * s, 60 * s, passo=16, colore=CELESTE, spessore=1.2)


def gimoto():
    f = Foglio(1440, 960, seme=201)
    f.testo(720, 70, "la tuta su misura", 56)
    cx = 600
    # sagoma tuta frontale
    f.ellisse(cx, 170, 46, 54, spessore=2.4)  # collo/testa indicativa
    f.linea([(cx - 60, 220), (cx - 190, 260), (cx - 240, 480), (cx - 220, 500), (cx - 150, 320), (cx - 120, 520),
             (cx - 130, 860), (cx - 40, 860), (cx, 560), (cx + 40, 860), (cx + 130, 860), (cx + 120, 520),
             (cx + 150, 320), (cx + 220, 500), (cx + 240, 480), (cx + 190, 260), (cx + 60, 220)], spessore=3.2)
    f.linea([(cx, 225), (cx, 540)], spessore=1.6, passate=1)  # zip
    # protezioni
    for (x, y) in ((cx - 175, 290), (cx + 175, 290), (cx - 215, 420), (cx + 215, 420)):
        f.ellisse(x, y, 26, 34, spessore=2, colore=CELESTE)
    f.rettangolo(cx - 120, 660, 70, 90, spessore=2.6, colore=CELESTE)  # saponetta
    f.rettangolo(cx + 50, 660, 70, 90, spessore=2.6, colore=CELESTE)
    # misure
    f.freccia(cx - 260, 240, cx - 260, 860, curva=0, spessore=1.6, punta=14)
    f.freccia(cx - 260, 860, cx - 260, 240, curva=0, spessore=1.6, punta=14)
    f.testo(cx - 290, 560, "misure prese su di te", 30, ruota=-90)
    etichetta(f, 960, 290, cx + 200, 290, "protezioni su spalle e gomiti")
    etichetta(f, 960, 420, cx + 240, 420, "airbag, se lo scegli")
    etichetta(f, 960, 700, cx + 120, 700, "saponette sulle ginocchia")
    etichetta(f, 960, 560, cx + 10, 520, "pelle, colori e grafica a scelta")
    f.testo(720, 920, "costruita sulle tue misure, non su una taglia", 32)
    return f.salva_png(USCITA / "gimoto-tuta.png")


def leovince():
    f = Foglio(1440, 760, seme=203)
    f.testo(720, 70, "il terminale di scarico", 56)
    # collettore e terminale
    f.linea([(120, 520), (300, 520), (380, 470), (480, 440)], spessore=3)
    f.linea([(120, 570), (300, 570), (390, 520), (480, 500)], spessore=3)
    f.linea([(480, 400), (1100, 330), (1180, 340), (1180, 520), (1100, 560), (480, 540), (480, 400)], spessore=3.4)
    f.linea([(560, 392), (560, 545)], spessore=1.6, passate=1)
    f.linea([(1040, 338), (1040, 555)], spessore=1.6, passate=1)
    f.tratteggio(564, 380, 470, 165, passo=14, colore=CELESTE, spessore=1.1)
    f.ellisse(1180, 430, 22, 90, spessore=2.6)
    f.ellisse(1180, 430, 10, 40, spessore=2)
    f.freccia(1220, 430, 1360, 410, spessore=2.2, colore=CELESTE)
    etichetta(f, 300, 260, 520, 420, "fascetta e raccordo", ancora="end")
    etichetta(f, 800, 220, 800, 370, "corpo in titanio, acciaio o carbonio")
    etichetta(f, 1200, 640, 1180, 520, "fondello e uscita")
    f.testo(720, 700, "schizzo indicativo: forme e materiali cambiano da modello a modello", 30)
    return f.salva_png(USCITA / "leovince-terminale.png")


def midland():
    f = Foglio(1440, 900, seme=205)
    f.testo(720, 70, "l'interfono sul casco", 56)
    casco_profilo(f, 520, 470, s=1.4)
    # interfono sul lato sinistro del casco
    f.rettangolo(330, 470, 130, 90, spessore=3, colore=CELESTE)
    f.ellisse(395, 515, 18, 18, spessore=2)
    f.linea([(395, 470), (395, 400)], spessore=2.4)  # antenna
    # onde
    for r in (60, 100, 140):
        pts = [(395 + r * math.cos(math.radians(a)), 400 + r * math.sin(math.radians(a))) for a in range(-150, -30, 5)]
        f.linea(pts, spessore=1.6, passate=1, colore=CELESTE)
    etichetta(f, 960, 280, 430, 480, "unità fissata al casco")
    etichetta(f, 960, 340, 400, 410, "radio: parli con altri motociclisti")
    f.testo(960, 560, "altoparlanti e microfono", 32, ancora="start")
    f.testo(960, 600, "dentro il casco", 32, ancora="start")
    f.testo(960, 660, "telefono, navigatore,", 32, ancora="start")
    f.testo(960, 700, "musica in Bluetooth", 32, ancora="start")
    f.testo(720, 850, "schizzo indicativo: ogni modello ha forma e funzioni diverse", 30)
    return f.salva_png(USCITA / "midland-interfono.png")


def onedesign():
    f = Foglio(1440, 860, seme=207)
    f.testo(720, 70, "il tank grip sul serbatoio", 56)
    # serbatoio visto di lato
    f.linea([(240, 560), (300, 340), (520, 250), (900, 250), (1120, 330), (1200, 560), (240, 560)], spessore=3.4)
    f.ellisse(700, 250, 70, 14, spessore=2.2)  # tappo
    # tank grip laterale
    f.linea([(860, 330), (1080, 360), (1140, 540), (880, 540), (860, 330)], spessore=3, colore=CELESTE)
    f.tratteggio(870, 345, 260, 190, passo=16, colore=CELESTE, spessore=1.2)
    # ginocchio
    f.ellisse(1010, 650, 90, 60, spessore=2.4)
    f.freccia(1010, 590, 1010, 520, spessore=2.2)
    etichetta(f, 300, 200, 900, 360, "adesivo in rilievo, ruvido al tatto", ancora="start")
    f.testo(1010, 760, "il ginocchio fa presa", 32)
    f.testo(500, 680, "più controllo in frenata", 32)
    f.testo(500, 720, "e niente graffi sul serbatoio", 32)
    return f.salva_png(USCITA / "onedesign-tankgrip.png")


def raceacademy():
    f = Foglio(1440, 900, seme=209)
    f.testo(720, 70, "una giornata in pista", 56)
    # tracciato inventato
    pts = []
    for i in range(0, 361, 4):
        a = math.radians(i)
        r = 260 + 70 * math.sin(2 * a) + 40 * math.cos(3 * a)
        pts.append((560 + 1.5 * r * math.cos(a), 470 + r * math.sin(a)))
    f.linea(pts, chiuso=True, spessore=4)
    f.linea([(p[0] * 0.92 + 45, p[1] * 0.92 + 38) for p in pts], chiuso=True, spessore=2, passate=1)
    # punti di riferimento
    for idx, t in ((8, "staccata"), (20, "corda"), (62, "uscita")):
        x, y = pts[idx]
        f.ellisse(x, y, 12, 12, spessore=2.4, colore=CELESTE)
        f.testo(x + 24, y - 14, t, 30, ancora="start")
    f.testo(1260, 300, "istruttore", 32)
    f.testo(1260, 340, "davanti", 32)
    f.testo(1260, 400, "allievo", 32)
    f.testo(1260, 440, "dietro", 32)
    f.testo(720, 860, "tracciato di fantasia: si impara a leggere staccata, corda e uscita", 30)
    return f.salva_png(USCITA / "raceacademy-pista.png")


def suomy():
    f = Foglio(1440, 860, seme=211)
    f.testo(720, 70, "il casco integrale", 56)
    casco_profilo(f, 600, 470, s=1.6)
    # spoiler
    f.ellisse(640, 230, 30, 10, spessore=2)
    etichetta(f, 1020, 220, 650, 230, "prese d'aria")
    etichetta(f, 1020, 330, 800, 360, "visiera")
    etichetta(f, 1020, 470, 870, 600, "mentoniera")
    etichetta(f, 220, 620, 340, 560, "calotta", ancora="end")
    f.testo(720, 810, "schizzo indicativo, non un modello specifico", 30)
    return f.salva_png(USCITA / "suomy-casco.png")


def prs():
    f = Foglio(1440, 900, seme=213)
    f.testo(720, 70, "si va in moto insieme", 56)
    # tre caschi visti di fronte, uno accanto all'altro
    for k, cx in enumerate((400, 720, 1040)):
        f.ellisse(cx, 400, 130, 150, spessore=3.2)
        f.linea([(cx - 100, 380), (cx + 100, 380), (cx + 90, 450), (cx - 90, 450), (cx - 100, 380)], spessore=2.6)
        f.tratteggio(cx - 90, 386, 180, 60, passo=16, colore=CELESTE, spessore=1.2)
        f.linea([(cx - 70, 560), (cx + 70, 560)], spessore=2.4)
    f.testo(400, 620, "chi ha appena iniziato", 30)
    f.testo(720, 620, "chi va in pista", 30)
    f.testo(1040, 620, "chi gira la domenica", 30)
    f.linea([(240, 700), (1200, 700)], spessore=2, colore=CELESTE)
    f.testo(720, 760, "prima il divertimento, poi la prestazione", 40)
    f.testo(720, 840, "uscite · pista con le pit bike · simulatore · workshop", 30)
    return f.salva_png(USCITA / "prs-insieme.png")


if __name__ == "__main__":
    USCITA.mkdir(parents=True, exist_ok=True)
    for fn in (gimoto, leovince, midland, onedesign, raceacademy, suomy, prs):
        print(fn())

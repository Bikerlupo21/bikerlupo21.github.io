"""Schizzi del gruppo Scarico. Avvio: python3 strumenti/schizzi/scarico.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, GRAFITE, RADICE, Foglio  # noqa: E402
from manovellismo import etichetta  # noqa: E402

USCITA = RADICE / "public/img/motore"


def tubo(f, pts, **kw):
    f.linea(pts, spessore=3.2, **kw)


def collettori():
    f = Foglio(1440, 980, seme=111)
    f.testo(720, 70, "collettori: 4 in 1 e 4-2-1", 56)
    for k, (x0, nome) in enumerate(((140, "4 in 1"), (820, "4-2-1"))):
        f.testo(x0 + 240, 150, nome, 46)
        # testata con 4 luci
        f.rettangolo(x0, 190, 480, 60, spessore=3)
        xs = [x0 + 60 + i * 120 for i in range(4)]
        for x in xs:
            f.ellisse(x, 250, 22, 10, spessore=2, passate=1)
        if k == 0:
            for x in xs:
                tubo(f, [(x, 260), (x, 480), (x0 + 240, 640)])
            tubo(f, [(x0 + 240, 640), (x0 + 240, 820)])
            f.testo(x0 + 280, 740, "un solo collettore", 28, ancora="start")
        else:
            tubo(f, [(xs[0], 260), (xs[0], 470), (x0 + 120, 560)])
            tubo(f, [(xs[3], 260), (xs[3], 470), (x0 + 360, 560)])
            tubo(f, [(xs[1], 260), (xs[1], 430), (x0 + 120, 560)])
            tubo(f, [(xs[2], 260), (xs[2], 430), (x0 + 360, 560)])
            tubo(f, [(x0 + 120, 560), (x0 + 120, 640), (x0 + 240, 720)])
            tubo(f, [(x0 + 360, 560), (x0 + 360, 640), (x0 + 240, 720)])
            tubo(f, [(x0 + 240, 720), (x0 + 240, 820)])
            f.testo(x0 + 400, 520, "a coppie", 28, ancora="start")
        # onda
        f.freccia(xs[0] - 40, 300, xs[0] - 40, 440, spessore=2, colore=CELESTE, punta=16)
        f.freccia(xs[0] - 70, 440, xs[0] - 70, 300, spessore=2, colore=CELESTE, punta=16)
    f.testo(130, 330, "onda", 28, ancora="end")
    f.testo(130, 362, "di pressione", 26, ancora="end")
    f.testo(130, 420, "onda riflessa", 26, ancora="end")
    f.testo(130, 450, "(depressione)", 26, ancora="end")
    f.testo(720, 890, "la lunghezza dei tubi decide a che regime l'onda riflessa aiuta a svuotare il cilindro", 30)
    return f.salva_png(USCITA / "collettori-scarico.png")


def catalizzatore():
    f = Foglio(1440, 880, seme=113)
    f.testo(720, 70, "il catalizzatore trivalente", 56)
    # involucro
    tubo(f, [(100, 400), (300, 400), (400, 300), (1040, 300), (1140, 400), (1340, 400)])
    tubo(f, [(100, 520), (300, 520), (400, 620), (1040, 620), (1140, 520), (1340, 520)])
    f.linea([(400, 300), (400, 620)], spessore=2)
    f.linea([(1040, 300), (1040, 620)], spessore=2)
    # nido d'ape
    for y in range(320, 620, 24):
        f.linea([(410, y), (1030, y)], spessore=1.2, passate=1)
    for x in range(430, 1030, 60):
        f.linea([(x, 310), (x, 610)], spessore=0.9, passate=1)
    f.tratteggio(404, 304, 632, 312, passo=22, colore=CELESTE, spessore=0.9)
    # gas
    f.freccia(120, 460, 280, 460, spessore=2.6)
    f.testo(200, 590, "CO · HC · NOx", 30)
    f.freccia(1160, 460, 1320, 460, spessore=2.6, colore=CELESTE)
    f.testo(1240, 590, "CO₂ · H₂O · N₂", 30)
    # sonda lambda
    f.rettangolo(230, 330, 30, 70, spessore=2.4)
    f.linea([(245, 330), (245, 260), (180, 230)], spessore=1.6, passate=1)
    f.testo(150, 220, "sonda lambda", 28)
    etichetta(f, 760, 180, 720, 310, "monolito a nido d'ape con metalli preziosi")
    f.testo(720, 700, "ossida CO e HC · riduce gli NOx", 34)
    f.testo(720, 750, "lavora bene solo caldo e con miscela vicina allo stechiometrico", 30)
    return f.salva_png(USCITA / "catalizzatore.png")


def silenziatore():
    f = Foglio(1440, 980, seme=115)
    f.testo(720, 70, "come si abbassa il rumore", 56)
    # assorbimento
    f.testo(720, 160, "assorbimento", 42)
    f.rettangolo(260, 200, 920, 200, spessore=3.2)
    f.linea([(160, 270), (1280, 270)], spessore=2.4)
    f.linea([(160, 330), (1280, 330)], spessore=2.4)
    for x in range(290, 1160, 40):
        f.ellisse(x, 270, 5, 4, spessore=1.2, passate=1)
        f.ellisse(x, 330, 5, 4, spessore=1.2, passate=1)
    f.tratteggio(264, 204, 912, 62, passo=10, colore=CELESTE, spessore=1.1)
    f.tratteggio(264, 334, 912, 62, passo=10, colore=CELESTE, spessore=1.1)
    f.freccia(100, 300, 240, 300, spessore=2.4)
    f.freccia(1200, 300, 1340, 300, spessore=2.4)
    etichetta(f, 1000, 450, 900, 380, "lana fonoassorbente", dim=30)
    etichetta(f, 300, 450, 400, 330, "tubo forato", ancora="end", dim=30)
    # riflessione
    f.testo(720, 560, "camere e riflessione", 42)
    f.rettangolo(260, 600, 920, 220, spessore=3.2)
    for x in (560, 880):
        f.linea([(x, 600), (x, 820)], spessore=2.4)
    tubo(f, [(160, 710), (420, 710)])
    tubo(f, [(380, 650), (1000, 650)])
    tubo(f, [(700, 770), (1280, 770)])
    f.freccia(100, 710, 240, 710, spessore=2.4)
    f.freccia(1200, 770, 1340, 770, spessore=2.4)
    for (x, y) in ((470, 760), (790, 700), (1060, 690)):
        f.freccia(x - 30, y + 20, x + 30, y - 20, curva=0.4, spessore=1.6, colore=CELESTE, punta=12)
    etichetta(f, 1000, 870, 880, 800, "paratie: dividono le camere", dim=30)
    return f.salva_png(USCITA / "silenziatore.png")


if __name__ == "__main__":
    for fn in (collettori, catalizzatore, silenziatore):
        print(fn())

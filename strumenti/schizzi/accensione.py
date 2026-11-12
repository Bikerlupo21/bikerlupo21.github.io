"""Schizzi del gruppo Accensione. Avvio: python3 strumenti/schizzi/accensione.py"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, GRAFITE, RADICE, Foglio  # noqa: E402
from manovellismo import etichetta  # noqa: E402

USCITA = RADICE / "public/img/motore"


def candela_disegno(f, cx, y0, scala=1.0, naso=110, etichette=True):
    """Candela vista in sezione, dall'alto (terminale) al basso (elettrodi)."""
    s = scala
    # terminale
    f.rettangolo(cx - 16 * s, y0, 32 * s, 50 * s, spessore=2.6)
    # isolante superiore con nervature
    yi = y0 + 50 * s
    f.linea([(cx - 34 * s, yi), (cx - 40 * s, yi + 230 * s)], spessore=3)
    f.linea([(cx + 34 * s, yi), (cx + 40 * s, yi + 230 * s)], spessore=3)
    f.linea([(cx - 34 * s, yi), (cx + 34 * s, yi)], spessore=2.6)
    for k in range(4):
        y = yi + (40 + k * 40) * s
        f.linea([(cx - 37 * s, y), (cx + 37 * s, y)], spessore=1.4, passate=1)
    # esagono
    ye = yi + 230 * s
    f.rettangolo(cx - 80 * s, ye, 160 * s, 80 * s, spessore=3.2)
    # guarnizione
    yg = ye + 80 * s
    f.rettangolo(cx - 66 * s, yg, 132 * s, 14 * s, spessore=2.2)
    # corpo filettato
    yf = yg + 14 * s
    hf = 150 * s
    f.linea([(cx - 56 * s, yf), (cx - 56 * s, yf + hf)], spessore=3)
    f.linea([(cx + 56 * s, yf), (cx + 56 * s, yf + hf)], spessore=3)
    for k in range(9):
        y = yf + (10 + k * 15) * s
        f.linea([(cx - 64 * s, y), (cx - 56 * s, y + 8 * s)], spessore=1.6, passate=1)
        f.linea([(cx + 56 * s, y), (cx + 64 * s, y + 8 * s)], spessore=1.6, passate=1)
    # naso dell'isolante (ceramica) dentro il corpo
    yb = yf + hf
    f.linea([(cx - 26 * s, ye + 20 * s), (cx - 26 * s, yb - naso * s), (cx - 14 * s, yb - 6 * s)], spessore=2.4)
    f.linea([(cx + 26 * s, ye + 20 * s), (cx + 26 * s, yb - naso * s), (cx + 14 * s, yb - 6 * s)], spessore=2.4)
    # elettrodo centrale
    f.linea([(cx, y0 + 50 * s), (cx, yb + 14 * s)], spessore=3, colore=GRAFITE)
    # elettrodo di massa
    f.linea([(cx + 56 * s, yb), (cx + 56 * s, yb + 44 * s), (cx - 10 * s, yb + 44 * s)], spessore=3.4)
    f.scintilla(cx - 2 * s, yb + 30 * s, r=24 * s, spessore=2, colore=CELESTE)
    return yb


def candela():
    f = Foglio(1440, 1000, seme=81)
    f.testo(720, 70, "la candela, in sezione", 56)
    cx = 520
    yb = candela_disegno(f, cx, 120, scala=1.25)
    etichetta(f, 820, 160, cx + 20, 150, "terminale: arriva l'alta tensione")
    etichetta(f, 820, 300, cx + 46, 300, "isolante in ceramica")
    etichetta(f, 820, 450, cx + 100, 450, "esagono per la chiave")
    etichetta(f, 820, 530, cx + 82, 530, "guarnizione")
    etichetta(f, 820, 610, cx + 76, 620, "filetto (si avvita nella testata)")
    etichetta(f, 820, 700, cx + 33, 700, "naso dell'isolante")
    etichetta(f, 820, 820, cx + 60, yb + 50, "elettrodo di massa")
    etichetta(f, 220, 760, cx - 6, 700, "elettrodo centrale", ancora="end")
    etichetta(f, 220, 860, cx - 6, yb + 38, "distanza elettrodi", ancora="end")
    f.testo(720, 960, "la scintilla scocca tra i due elettrodi e accende la miscela", 32)
    return f.salva_png(USCITA / "candela-sezione.png")


def grado_termico():
    f = Foglio(1440, 900, seme=83)
    f.testo(720, 70, "candela calda e candela fredda", 56)
    for cx, nome, naso, nota in ((400, "calda", 150, "naso lungo: il calore fa più strada"),
                                (1040, "fredda", 60, "naso corto: il calore esce prima")):
        f.testo(cx, 150, nome, 48)
        # corpo della candela (parte bassa) in sezione
        top, bot = 230, 680
        f.linea([(cx - 130, top), (cx - 130, bot)], spessore=3.2)
        f.linea([(cx + 130, top), (cx + 130, bot)], spessore=3.2)
        # isolante
        yn = bot - naso * 2.4
        f.linea([(cx - 60, top), (cx - 60, yn), (cx - 30, bot - 20)], spessore=2.8)
        f.linea([(cx + 60, top), (cx + 60, yn), (cx + 30, bot - 20)], spessore=2.8)
        f.linea([(cx - 130, yn), (cx - 60, yn)], spessore=2.4)
        f.linea([(cx + 60, yn), (cx + 130, yn)], spessore=2.4)
        f.tratteggio(cx - 128, top + 2, 66, yn - top - 4, passo=12, spessore=1.2)
        f.tratteggio(cx + 62, top + 2, 66, yn - top - 4, passo=12, spessore=1.2)
        f.linea([(cx, top), (cx, bot + 10)], spessore=3)
        # percorso del calore
        f.freccia(cx - 20, bot - 30, cx - 44, yn + 10, curva=0.1, spessore=2.4, colore=CELESTE)
        f.freccia(cx - 70, yn - 10, cx - 140, yn - 60, curva=0.0, spessore=2.4, colore=CELESTE)
        f.testo(cx, 760, nota, 32)
    f.testo(720, 850, "il grado termico dice quanto in fretta la punta smaltisce il calore verso la testata", 30)
    return f.salva_png(USCITA / "candela-grado-termico.png")


def bobina():
    f = Foglio(1440, 900, seme=85)
    f.testo(720, 70, "la bobina: da pochi volt a migliaia", 56)
    # nucleo
    f.rettangolo(560, 200, 60, 460, spessore=3)
    f.tratteggio(562, 202, 56, 456, passo=14, spessore=1.2)
    # secondario (tante spire fitte)
    pts = []
    for i in range(0, 361):
        t = i / 360
        pts.append((590 + 70 * math.sin(t * math.tau * 30), 230 + t * 400))
    f.linea(pts, spessore=1.1, passate=1, colore=GRAFITE)
    # primario (poche spire grosse)
    pts = []
    for i in range(0, 121):
        t = i / 120
        pts.append((590 + 110 * math.sin(t * math.tau * 5), 250 + t * 360))
    f.linea(pts, spessore=3.4, passate=2, colore=CELESTE)
    etichetta(f, 820, 260, 700, 280, "primario: poche spire di filo grosso")
    etichetta(f, 820, 340, 660, 360, "secondario: migliaia di spire sottili")
    etichetta(f, 820, 420, 620, 440, "nucleo di ferro")
    # circuito primario
    f.linea([(480, 250), (300, 250), (300, 330)], spessore=2.4, colore=CELESTE)
    f.rettangolo(200, 330, 200, 90, spessore=2.6)
    f.testo(300, 385, "batteria 12 V", 30)
    f.linea([(480, 610), (300, 610), (300, 560)], spessore=2.4, colore=CELESTE)
    f.rettangolo(200, 470, 200, 90, spessore=2.6)
    f.testo(300, 512, "interruttore", 30)
    f.testo(300, 545, "(centralina)", 28)
    # uscita alta tensione
    f.linea([(590, 660), (590, 740), (900, 740)], spessore=2.8)
    f.testo(745, 725, "alta tensione", 30)
    candela_mini_x = 960
    f.rettangolo(900, 715, 120, 50, spessore=2.6)
    f.testo(960, 800, "candela", 30)
    f.scintilla(1050, 740, r=20, colore=CELESTE, spessore=1.8)
    f.testo(1100, 560, "corrente nel primario", 30, ancora="start")
    f.testo(1100, 595, "→ campo magnetico", 30, ancora="start")
    f.testo(1100, 630, "si interrompe di colpo", 30, ancora="start")
    f.testo(1100, 665, "→ alta tensione nel secondario", 30, ancora="start")
    f.testo(720, 860, "schema di principio: le spire sono molte di più di quelle disegnate", 30)
    return f.salva_png(USCITA / "bobina-schema.png")


def centralina():
    f = Foglio(1440, 900, seme=87)
    f.testo(720, 70, "chi decide quando scocca la scintilla", 54)
    # volano con riferimento
    cx, cy, r = 260, 420, 150
    f.ellisse(cx, cy, r, r, giri=1.05, spessore=3.2)
    f.ellisse(cx, cy, 20, 20, spessore=2, passate=1)
    a = math.radians(-40)
    f.rettangolo(cx + (r - 6) * math.cos(a) - 14, cy + (r - 6) * math.sin(a) - 14, 28, 28, spessore=2.4)
    f.freccia(cx - 60, cy - r - 40, cx + 60, cy - r - 40, curva=0.2, spessore=2, punta=16)
    f.testo(cx, 640, "volano / albero motore", 32)
    # pick-up
    f.rettangolo(cx + 170, cy - 170, 70, 60, spessore=2.6)
    f.testo(cx + 205, cy - 195, "pick-up", 30)
    f.linea([(cx + 240, cy - 140), (560, cy - 60)], spessore=2, colore=CELESTE)
    # centralina
    f.rettangolo(560, 300, 300, 220, spessore=3.4)
    f.testo(710, 370, "centralina", 42)
    f.testo(710, 420, "giri + carico", 30)
    f.testo(710, 460, "→ anticipo", 30)
    f.testo(710, 500, "limitatore", 28)
    # altri ingressi
    f.linea([(710, 200), (710, 300)], spessore=2, colore=CELESTE)
    f.testo(710, 185, "farfalla, temperatura, marcia...", 28)
    # uscita
    f.freccia(870, 410, 1060, 410, spessore=2.6)
    f.rettangolo(1070, 360, 130, 100, spessore=2.8)
    f.testo(1135, 418, "bobina", 30)
    f.linea([(1200, 410), (1290, 410)], spessore=2.6)
    f.scintilla(1320, 410, r=22, colore=CELESTE, spessore=1.8)
    # curva anticipo qualitativa
    ox, oy = 600, 780
    f.linea([(ox, oy), (ox + 420, oy)], spessore=2)
    f.linea([(ox, oy), (ox, oy - 170)], spessore=2)
    f.linea([(ox, oy - 40), (ox + 60, oy - 40), (ox + 220, oy - 140), (ox + 400, oy - 150)], spessore=3, colore=CELESTE)
    f.testo(ox + 210, oy + 40, "giri", 28)
    f.testo(ox - 20, oy - 180, "anticipo", 28, ancora="end")
    f.testo(ox + 460, oy - 120, "esempio di curva:", 28, ancora="start")
    f.testo(ox + 460, oy - 85, "la forma cambia", 28, ancora="start")
    f.testo(ox + 460, oy - 50, "da motore a motore", 28, ancora="start")
    return f.salva_png(USCITA / "centralina-accensione.png")


if __name__ == "__main__":
    for fn in (candela, grado_termico, bobina, centralina):
        print(fn())

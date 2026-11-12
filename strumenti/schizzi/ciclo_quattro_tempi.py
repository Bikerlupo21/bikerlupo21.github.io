"""Schizzi per l'articolo "Il ciclo a quattro tempi". Avvio: python3 strumenti/schizzi/ciclo_quattro_tempi.py"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, GRAFITE, RADICE, Foglio  # noqa: E402

USCITA = RADICE / "public/img/motore"


def pannello(f: Foglio, ox, oy, n, nome, theta_gradi, asp_aperta, sca_aperta, verso, didascalie, gas=None, scintilla=False):
    """Un cilindro in sezione. theta = angolo di manovella (0 = PMS), rotazione oraria."""
    cx = ox + 340
    f.testo(cx, oy + 48, f"{n} · {nome}", 60, ruota=-1)

    # testata con condotti
    ht, hb = oy + 160, oy + 240
    f.linea([(ox + 150, hb), (ox + 150, ht), (ox + 530, ht), (ox + 530, hb)])
    f.linea([(ox + 150, hb), (ox + 215, hb)])
    f.linea([(ox + 465, hb), (ox + 530, hb)])
    # condotto aspirazione (sinistra) ed scarico (destra)
    f.linea([(ox + 215, hb), (ox + 150, ht + 20)], spessore=2.6)
    f.linea([(ox + 305, hb), (ox + 230, ht - 30), (ox + 120, ht - 30)], spessore=2.6)
    f.linea([(ox + 465, hb), (ox + 530, ht + 20)], spessore=2.6)
    f.linea([(ox + 375, hb), (ox + 450, ht - 30), (ox + 560, ht - 30)], spessore=2.6)
    f.testo(ox + 95, ht - 45, "asp.", 34, ancora="middle")
    f.testo(ox + 590, ht - 45, "scar.", 34, ancora="middle")

    # valvole: chiusa = fungo sulla sede, aperta = fungo abbassato nel cilindro
    for xv, aperta in ((ox + 260, asp_aperta), (ox + 420, sca_aperta)):
        y = hb + (34 if aperta else 0)
        f.linea([(xv, ht - 50), (xv, y - 6)], spessore=3.4)
        f.linea([(xv - 42, y), (xv - 6, y - 10), (xv + 6, y - 10), (xv + 42, y)], spessore=3.6)

    # candela al centro
    f.linea([(cx - 12, ht - 50), (cx - 12, hb - 4)], spessore=2.6)
    f.linea([(cx + 12, ht - 50), (cx + 12, hb - 4)], spessore=2.6)
    f.linea([(cx - 20, ht - 50), (cx + 20, ht - 50)], spessore=2.6)
    if scintilla:
        f.scintilla(cx, hb + 14, 30, spessore=2.6)

    # cilindro
    fondo = oy + 650
    f.linea([(ox + 190, hb), (ox + 190, fondo)])
    f.linea([(ox + 490, hb), (ox + 490, fondo)])

    # manovellismo: albero, biella, pistone
    ccy, r, L = oy + 730, 75, 280
    t = math.radians(theta_gradi)
    px, py = cx + r * math.sin(t), ccy - r * math.cos(t)
    spin = py - math.sqrt(L * L - (r * math.sin(t)) ** 2)
    ptop = spin - 40
    # gas sopra il pistone
    if gas == "fresco":
        f.tratteggio(ox + 196, hb + 6, 288, ptop - hb - 12, passo=16, colore=CELESTE, spessore=2.2)
    elif gas == "compresso":
        f.tratteggio(ox + 196, hb + 6, 288, ptop - hb - 12, passo=7, colore=CELESTE, spessore=2.2)
    elif gas == "combusto":
        f.tratteggio(ox + 196, hb + 6, 288, ptop - hb - 12, passo=10, angolo=35, spessore=1.8)
    elif gas == "scarico":
        f.tratteggio(ox + 196, hb + 6, 288, ptop - hb - 12, passo=18, angolo=35, spessore=1.6)
    f.rettangolo(ox + 200, ptop, 280, 90, spessore=3.4)
    f.linea([(ox + 204, ptop + 16), (ox + 476, ptop + 16)], spessore=1.8)
    f.linea([(ox + 204, ptop + 28), (ox + 476, ptop + 28)], spessore=1.8)
    f.ellisse(cx, spin, 14, 14, spessore=2.4)
    f.linea([(cx, spin), (px, py)], spessore=5)
    f.ellisse(cx, ccy, 22, 22, spessore=2.6)  # asse albero
    f.linea([(cx, ccy), (px, py)], spessore=6)  # manovella
    f.ellisse(px, py, 12, 12, spessore=2.4)
    f.ellisse(cx, ccy, 118, 92, spessore=2.2)  # carter
    # verso di rotazione (orario)
    a0, a1 = math.radians(-60), math.radians(10)
    f.freccia(cx + 140 * math.cos(a0), ccy + 112 * math.sin(a0), cx + 140 * math.cos(a1), ccy + 112 * math.sin(a1), curva=-0.25, punta=16, spessore=2.2)

    # movimento del pistone
    if verso == "giu":
        f.freccia(ox + 560, ptop + 10, ox + 560, ptop + 140, curva=0.05, spessore=3.4)
    else:
        f.freccia(ox + 560, ptop + 140, ox + 560, ptop + 10, curva=0.05, spessore=3.4)

    # flussi
    if gas == "fresco":
        f.freccia(ox + 110, ht - 10, ox + 245, hb + 70, curva=-0.2, colore=CELESTE, spessore=3.6)
    if gas == "scarico":
        f.freccia(ox + 430, hb + 70, ox + 590, ht - 10, curva=-0.2, spessore=3.4)
    if gas == "combusto":
        for dx in (-80, 0, 80):
            f.freccia(cx + dx, hb + 30, cx + dx, ptop - 12, curva=0.0, punta=16, spessore=2.6)

    for i, riga in enumerate(didascalie):
        f.testo(cx, oy + 890 + i * 46, riga, 38)


def quattro_fasi():
    f = Foglio(1440, 2100, seme=4)
    pannello(f, 30, 30, 1, "aspirazione", 150, True, False, "giu",
             ["pistone: scende (PMS → PMI)", "aspirazione aperta · scarico chiuso"], gas="fresco")
    pannello(f, 750, 30, 2, "compressione", 300, False, False, "su",
             ["pistone: sale (PMI → PMS)", "valvole chiuse"], gas="compresso")
    pannello(f, 30, 1050, 3, "espansione", 35, False, False, "giu",
             ["scintilla poco prima del PMS", "valvole chiuse · l'unica fase che spinge"], gas="combusto", scintilla=True)
    pannello(f, 750, 1050, 4, "scarico", 250, False, True, "su",
             ["pistone: sale (PMI → PMS)", "scarico aperto · aspirazione chiusa"], gas="scarico")
    f.linea([(720, 60), (722, 2010)], spessore=1.4, passate=1)
    f.linea([(60, 1035), (1380, 1033)], spessore=1.4, passate=1)
    return f.salva_png(USCITA / "quattro-tempi-fasi.png")


def due_giri():
    f = Foglio(1440, 760, seme=9)
    f.testo(720, 70, "un ciclo = due giri dell'albero motore (720°)", 58)
    for k, (cx, giro, fase_dx, fase_sx) in enumerate(((380, "1° giro", "aspirazione", "compressione"),
                                                      (1060, "2° giro", "espansione", "scarico"))):
        cy, R = 400, 210
        f.ellisse(cx, cy, R, R, spessore=3.4)
        f.linea([(cx, cy - R - 24), (cx, cy + R + 24)], spessore=2)
        f.testo(cx, cy - R - 34, "PMS", 40)
        f.testo(cx, cy + R + 62, "PMI", 40)
        f.testo(cx + R * 0.52, cy + 10, fase_dx, 44 if len(fase_dx) < 12 else 38)
        f.testo(cx - R * 0.52, cy + 10, fase_sx, 44 if len(fase_sx) < 12 else 38)
        f.testo(cx, cy + R + 110, giro, 48)
        # verso orario: freccia sul lato destro
        a0, a1 = math.radians(-60), math.radians(-10)
        f.freccia(cx + (R + 30) * math.cos(a0), cy + (R + 30) * math.sin(a0),
                  cx + (R + 30) * math.cos(a1), cy + (R + 30) * math.sin(a1), curva=-0.25, punta=18, spessore=2.6)
        if k == 0:
            # scintilla poco prima del PMS, alla fine della compressione
            a = math.radians(-105)
            sx, sy = cx + R * math.cos(a), cy + R * math.sin(a)
            f.scintilla(sx, sy, 24, colore=CELESTE, spessore=3)
            f.testo(sx - 70, sy - 26, "scintilla", 38, colore=GRAFITE, ancora="end")
    f.testo(720, 420, "→", 70)
    return f.salva_png(USCITA / "quattro-tempi-due-giri.png")


def anticipo():
    f = Foglio(1440, 820, seme=12)
    f.testo(720, 70, "perché la scintilla arriva prima del PMS", 58)
    x0, x1, yb = 140, 1300, 640
    f.freccia(x0, yb, x1, yb, curva=0, spessore=3)
    f.freccia(x0, yb, x0, 150, curva=0, spessore=3)
    f.testo(x1 - 20, yb + 56, "rotazione dell'albero →", 38, ancora="end")
    f.testo(x0 + 18, 170, "pressione nel cilindro", 38, ancora="start")
    pms = 700
    for y in range(170, yb, 34):
        f.linea([(pms, y), (pms, y + 16)], spessore=2, passate=1)
    f.testo(pms, yb + 56, "PMS", 44)
    # curva qualitativa: sale, picco poco dopo il PMS, scende
    pts = []
    for i in range(0, 61):
        x = x0 + 40 + i * (x1 - x0 - 120) / 60
        u = (x - (pms + 70)) / 150
        y = yb - 20 - 370 * math.exp(-u * u) - 60 * math.exp(-((x - pms) / 260) ** 2)
        pts.append((x, y))
    f.linea(pts, spessore=4)
    # scintilla prima del PMS
    sx = pms - 170
    f.scintilla(sx, yb - 120, 26, colore=CELESTE, spessore=3)
    f.testo(sx - 30, yb - 170, "scintilla", 42, ancora="end")
    f.testo(sx - 30, yb - 128, "(prima del PMS)", 34, ancora="end")
    # picco
    f.ellisse(pms + 70, yb - 410, 46, 30, spessore=2.4)
    f.freccia(pms + 300, 330, pms + 125, yb - 405, curva=0.15, spessore=2.6)
    f.testo(pms + 310, 300, "pressione massima", 42, ancora="start")
    f.testo(pms + 310, 345, "poco dopo il PMS", 38, ancora="start")
    f.testo(720, 770, "la miscela ha bisogno di tempo per bruciare · schema qualitativo, senza valori", 34)
    return f.salva_png(USCITA / "quattro-tempi-anticipo.png")


if __name__ == "__main__":
    for fn in (quattro_fasi, due_giri, anticipo):
        print(fn())

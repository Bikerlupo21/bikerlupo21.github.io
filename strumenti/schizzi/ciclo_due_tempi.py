"""Schizzi per l'articolo "Il ciclo a due tempi". Avvio: python3 strumenti/schizzi/ciclo_due_tempi.py"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from matita import CELESTE, GRAFITE, RADICE, Foglio  # noqa: E402

USCITA = RADICE / "public/img/motore"


def pannello(f: Foglio, ox, oy, n, nome, theta, sopra, sotto, lamelle_aperte, didascalie, scintilla=False, verso="giu"):
    """Monocilindrico 2T con travaso a sinistra, scarico a destra, lamelle nel carter. theta: 0 = PMS, orario."""
    cx = ox + 340
    f.testo(cx, oy + 48, f"{n} · {nome}", 58, ruota=-1)

    ht, hb = oy + 110, oy + 170          # testata
    xl, xr = ox + 220, ox + 460          # pareti del cilindro
    fondo = oy + 540
    # testata con candela
    f.linea([(xl - 20, hb), (xl - 20, ht), (xr + 20, ht), (xr + 20, hb), (xl - 20, hb)])
    f.linea([(cx - 10, ht - 50), (cx - 10, ht)], spessore=2.6)
    f.linea([(cx + 10, ht - 50), (cx + 10, ht)], spessore=2.6)
    f.linea([(cx - 18, ht - 50), (cx + 18, ht - 50)], spessore=2.6)
    if scintilla:
        f.scintilla(cx, hb + 16, 30, colore=CELESTE, spessore=3)

    # luci: scarico (destra) più alta del travaso (sinistra) -> lo scarico apre per primo
    sca_top, sca_bot = oy + 330, oy + 445
    tra_top, tra_bot = oy + 375, oy + 450
    # parete destra con luce di scarico e condotto
    f.linea([(xr, hb), (xr, sca_top)])
    f.linea([(xr, sca_bot), (xr, fondo)])
    f.linea([(xr, sca_top), (xr + 90, sca_top - 20), (ox + 640, sca_top - 20)], spessore=2.8)
    f.linea([(xr, sca_bot), (xr + 90, sca_bot - 10), (ox + 640, sca_bot - 10)], spessore=2.8)
    f.testo(ox + 600, sca_top - 40, "scarico", 32)
    # parete sinistra con luce di travaso e condotto che scende al carter
    f.linea([(xl, hb), (xl, tra_top)])
    f.linea([(xl, tra_bot), (xl, fondo)])
    f.linea([(xl, tra_top), (xl - 70, tra_top + 10), (xl - 70, fondo + 40)], spessore=2.6)
    f.linea([(xl, tra_bot), (xl - 30, tra_bot + 6), (xl - 30, fondo + 30)], spessore=2.6)
    f.testo(xl - 92, tra_top - 22, "travaso", 30, ancora="end")

    # carter
    ccy, r, L = oy + 640, 110, 260
    f.linea([(xl - 70, fondo + 40), (ox + 130, fondo + 60), (ox + 120, ccy + 110), (cx, ccy + 150),
             (ox + 560, ccy + 110), (ox + 550, fondo + 50), (xr, fondo)], spessore=3.2)
    # lamelle (ingresso nel carter, in basso a sinistra)
    lx, ly = ox + 120, ccy + 40
    f.linea([(ox + 20, ly - 40), (lx, ly - 40)], spessore=2.6)
    f.linea([(ox + 20, ly + 40), (lx, ly + 40)], spessore=2.6)
    if lamelle_aperte:
        f.linea([(lx, ly - 34), (lx + 44, ly - 8)], spessore=2.6, colore=GRAFITE)
        f.linea([(lx, ly + 34), (lx + 44, ly + 8)], spessore=2.6, colore=GRAFITE)
        f.freccia(ox + 10, ly, lx + 60, ly, curva=0, punta=16, colore=CELESTE, spessore=3.2)
    else:
        f.linea([(lx, ly - 34), (lx + 30, ly)], spessore=2.6)
        f.linea([(lx, ly + 34), (lx + 30, ly)], spessore=2.6)
    f.testo(ox + 70, ly + 82, "lamelle", 30)

    # albero, biella, pistone
    t = math.radians(theta)
    px, py = cx + r * math.sin(t), ccy - r * math.cos(t)
    spin = py - math.sqrt(L * L - (r * math.sin(t)) ** 2)
    ptop = spin - 50
    pbot = ptop + 120  # pistone alto: il mantello copre/scopre le luci
    # gas sopra il pistone
    h_gas = ptop - hb - 8
    if sopra == "fresco":
        f.tratteggio(xl + 6, hb + 4, xr - xl - 12, h_gas, passo=8, colore=CELESTE, spessore=2)
    elif sopra == "combusto":
        f.tratteggio(xl + 6, hb + 4, xr - xl - 12, h_gas, passo=10, angolo=35, spessore=1.8)
        for dx in (-70, 0, 70):
            f.freccia(cx + dx, hb + 30, cx + dx, ptop - 12, curva=0, punta=14, spessore=2.4)
    elif sopra == "lavaggio":
        f.tratteggio(xl + 6, hb + 4, xr - xl - 12, h_gas, passo=16, angolo=35, spessore=1.4)
        f.freccia(xl - 50, tra_bot + 40, xl + 40, hb + 60, curva=-0.35, colore=CELESTE, spessore=3.4)
        f.freccia(cx + 20, hb + 50, xr + 120, sca_top + 10, curva=-0.25, spessore=3)
    # carica nel carter
    if sotto == "aspira":
        f.testo(cx + 40, ccy + 195, "il carter aspira", 30)
    elif sotto == "comprime":
        f.tratteggio(ox + 165, ccy - 30, 60, 70, passo=8, colore=CELESTE, spessore=1.8)
        f.testo(cx + 40, ccy + 195, "il carter comprime", 30)
    f.rettangolo(xl + 8, ptop, xr - xl - 16, pbot - ptop, spessore=3.2)
    f.linea([(xl + 12, ptop + 14), (xr - 12, ptop + 14)], spessore=1.6)
    f.ellisse(cx, spin, 13, 13, spessore=2.2)
    f.linea([(cx, spin), (px, py)], spessore=5)
    f.ellisse(cx, ccy, 20, 20, spessore=2.4)
    f.linea([(cx, ccy), (px, py)], spessore=6)
    f.ellisse(px, py, 11, 11, spessore=2.2)
    # verso del pistone
    if verso == "giu":
        f.freccia(ox + 640, oy + 480, ox + 640, oy + 590, curva=0.05, spessore=3.2)
    else:
        f.freccia(ox + 640, oy + 590, ox + 640, oy + 480, curva=0.05, spessore=3.2)

    for i, riga in enumerate(didascalie):
        f.testo(cx, oy + 900 + i * 44, riga, 36)


def fasi():
    f = Foglio(1440, 2120, seme=22)
    pannello(f, 30, 30, 1, "il pistone sale", 290, "fresco", "aspira", True,
             ["sopra: luci chiuse, comprime la miscela", "sotto: il carter aspira dalle lamelle"], verso="su")
    pannello(f, 750, 30, 2, "vicino al PMS", 345, "fresco", "aspira", True,
             ["scintilla poco prima del PMS", "sotto: il carter finisce di riempirsi"], scintilla=True, verso="su")
    pannello(f, 30, 1070, 3, "il pistone scende", 70, "combusto", "comprime", False,
             ["sopra: i gas spingono il pistone", "sotto: lamelle chiuse, il carter comprime"])
    pannello(f, 750, 1070, 4, "vicino al PMI", 170, "lavaggio", "comprime", False,
             ["si apre prima lo scarico, poi il travaso", "la carica fresca spinge fuori i gas"])
    f.linea([(720, 60), (722, 2030)], spessore=1.4, passate=1)
    f.linea([(60, 1050), (1380, 1048)], spessore=1.4, passate=1)
    return f.salva_png(USCITA / "due-tempi-fasi.png")


def spinte():
    f = Foglio(1440, 900, seme=5)
    f.testo(720, 70, "quante spinte in due giri dell'albero", 56)
    righe = (("4 tempi", 290, [True, False]), ("2 tempi", 650, [True, True]))
    for nome, cy, sp in righe:
        f.testo(170, cy + 14, nome, 50)
        for k, s_ in enumerate(sp):
            cx = 560 + k * 360
            f.ellisse(cx, cy, 110, 110, spessore=3)
            f.testo(cx, cy + 160, f"{k + 1}° giro", 36)
            f.testo(cx + 40, cy - 128, "PMS", 30)
            f.linea([(cx, cy - 122), (cx, cy - 98)], spessore=1.8, passate=1)
            if s_:
                f.scintilla(cx - 24, cy - 108, 22, colore=CELESTE, spessore=3)
                f.testo(cx, cy + 12, "spinta", 40)
            else:
                f.testo(cx, cy + 12, "nessuna spinta", 32)
        f.freccia(690, cy, 770, cy, curva=0, punta=16, spessore=2.4)
    f.testo(1240, 300, "1 spinta ogni 2 giri", 38)
    f.testo(1240, 660, "1 spinta a ogni giro", 38)
    return f.salva_png(USCITA / "due-tempi-spinte.png")


def espansione():
    f = Foglio(1440, 820, seme=8)
    f.testo(720, 70, "la marmitta ad espansione", 58)
    y = 420
    alto = [(120, y - 62), (340, y - 66), (620, y - 180), (900, y - 180), (1160, y - 60), (1340, y - 40)]
    basso = [(120, y + 62), (340, y + 66), (620, y + 180), (900, y + 180), (1160, y + 60), (1340, y + 40)]
    f.linea(alto, spessore=3.4)
    f.linea(basso, spessore=3.4)
    f.linea([(120, y - 90), (120, y + 90)], spessore=2.6)
    f.testo(110, y + 135, "luce di", 32)
    f.testo(110, y + 170, "scarico", 32)
    f.testo(230, y - 84, "collettore", 32)
    f.testo(470, y - 170, "cono divergente", 32, ruota=-20)
    f.testo(760, y - 200, "parte centrale", 32)
    f.testo(1060, y - 160, "cono convergente", 32, ruota=22)
    f.testo(1290, y - 62, "codino", 32)
    # onda in uscita e le due onde di ritorno (dentro al tubo)
    f.freccia(160, y, 1200, y, curva=0.0, punta=18, spessore=2.6)
    f.testo(760, y - 14, "onda dei gas di scarico", 30)
    f.freccia(560, y - 36, 150, y - 36, curva=0.0, punta=16, spessore=2.4)
    f.testo(520, y - 50, "1", 34)
    f.freccia(1100, y + 40, 150, y + 40, curva=0.0, punta=16, colore=CELESTE, spessore=3)
    f.testo(1080, y + 30, "2", 34)
    f.testo(720, y + 240, "1 · dal cono divergente torna un'onda che aiuta a svuotare il cilindro", 32)
    f.testo(720, y + 285, "2 · dal cono convergente torna un'onda che rispinge nel cilindro la carica fresca scappata", 32)
    f.testo(720, y + 350, "funziona al meglio solo in un certo intervallo di giri · schema qualitativo", 30)
    return f.salva_png(USCITA / "due-tempi-espansione.png")


if __name__ == "__main__":
    for fn in (fasi, spinte, espansione):
        print(fn())

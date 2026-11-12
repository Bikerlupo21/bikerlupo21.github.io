# Sito Bikerlupo (Astro)

## Provarlo sul tuo computer
1. Installa Node.js (versione 22 o successiva) da nodejs.org.
2. Apri il terminale in questa cartella e lancia:
   ```
   npm install
   npm run dev
   ```
3. Apri http://localhost:4321. In locale vedi anche le bozze.

## Dove si scrive
Ogni articolo è un file `.md` in `src/content/`:

| Cartella | Cosa contiene |
|---|---|
| `articoli/` | "Dal video" e "Provato da me" (campo `rubrica`) |
| `progetti/` | la pagina madre di ogni progetto |
| `puntate/` | le puntate (campo `progetto` = nome del file del progetto) |
| `motore/` | gli articoli "Il motore": servono almeno 2 fonti, altrimenti il sito non si compila |
| `brand/` | una scheda per brand |

- Per collegare un contenuto a un brand: `brand: [nome-file-del-brand]`. Comparirà da solo nella scheda del brand.
- `bozza: true` = il contenuto non va online (lo vedi solo in locale).
- Le foto vanno in `public/img/...` e si inseriscono con `![descrizione](/img/cartella/foto.jpg)`.
- Una riga che inizia con `>` diventa il box "nota a matita".
- I file che iniziano con `esempio-` sono modelli: copiali, poi cancellali.

## Dati generali
- Link ai social: `src/lib/sito.ts`
- Indirizzo del sito (o futuro dominio): `site` in `astro.config.mjs`
- Colori: `src/styles/global.css`

## Online
- Sito: https://bikerlupo21.github.io
- Pannello per scrivere: https://app.pagescms.org (entra con l'account GitHub bikerlupo21)
- Ogni modifica salvata su GitHub (dal pannello, da Claude o a mano) ripubblica il sito da sola in 1-2 minuti (`.github/workflows/deploy.yml`).

## Grafiche a matita (template per tutti gli articoli)
`strumenti/schizzi/matita.py` disegna in stile schizzo a matita su foglio bianco (grafite, Caveat, timbro BL21).
Ogni articolo ha il suo script, es. `strumenti/schizzi/ciclo_quattro_tempi.py`, che salva le PNG in `public/img/...`.

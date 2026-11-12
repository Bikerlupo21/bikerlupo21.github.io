---
titolo: "Centralina"
descrizione: "Come la centralina sa quando far scoccare la scintilla: pick-up sul volano, anticipo fisso o variabile, mappe e limitatore di giri."
data: 2026-11-12
gruppo: accensione
ordine: 3
verificatoIl: 2026-11-12
bozza: false
copertina: /img/motore/centralina-accensione.png
inBreve:
  - "Il pick-up legge la posizione dell'albero motore e avvisa la centralina."
  - "La centralina calcola l'anticipo e comanda la bobina nel momento giusto."
  - "Può avere anticipo fisso o variabile e di solito integra il limitatore di giri."
glossario:
  - { termine: "Pick-up", definizione: "Sensore che rileva il passaggio di un riferimento sul volano e manda un impulso alla centralina." }
  - { termine: "Anticipo di accensione", definizione: "Quanti gradi prima del punto morto superiore scocca la scintilla." }
  - { termine: "Curva di anticipo", definizione: "Come cambia l'anticipo al variare dei giri (e, nelle centraline più evolute, del carico)." }
  - { termine: "Limitatore di giri", definizione: "La funzione che taglia l'accensione quando il motore supera un certo regime." }
fonti:
  - { testo: "Motoclub Tingavert, «L'accensione dello scooter a statore-volano e a rotore interno»", link: "https://www.motoclub-tingavert.it/a3148s.html" }
  - { testo: "Motoclub Tingavert, centraline ad anticipo fisso e variabile", link: "https://www.motoclub-tingavert.it/a2529s.html" }
  - { testo: "Motoclub Tingavert, «L'anticipo di accensione»", link: "https://www.motoclub-tingavert.it/a290s.html" }
  - { testo: "Athena, istruzioni centralina NR-01 ad anticipo variabile (PDF)", link: "https://static.pedparts.co.uk/c/asset/instructions/S410480392003.pdf" }
  - { testo: "Malossi, istruzioni accensione MHR Team (PDF)", link: "https://medien.scootertech.at/files/Montageanleitung_Malossi_5514398.pdf" }
  - { testo: "FMS2, «Centralina scooter 50: originale, sbloccata, racing»", link: "https://www.fms2.com/blog/centralina-scooter-50-originale-sbloccata-racing-cosa-cambia-davvero.aspx" }
  - { testo: "FMS2, «Pick-up accensione: cos'è, sintomi, differenza con statore e bobina»", link: "https://www.fms2.com/blog/pick-up-accensione-cos-e-sintomi-differenza-statore-bobina.aspx" }
  - { testo: "InSella, «L'accensione digitale Polini for Race»", link: "https://www.insella.it/news/aumentano-potenza-accelerazione-laccensione-digitale-polini-for-race-66085" }
  - { testo: "Dynatek, FAQ: curve di anticipo e carico", link: "https://www.motorcycleid.com/dynatek/info/faq.html" }
  - { testo: "Pazon, accensione Smart-Fire (curva mappata e limitatore)", link: "https://pazon.com/products/product-list/smart-fire-ignitions/smart-fire-crank-trig-twin-4-stroke" }
  - { testo: "UTI, «Motorcycle Ignition Systems»", link: "https://uti.edu/blog/motorcycle/motorcycle-ignition-systems" }
---

La [bobina](/motore/bobina/) sa fare l'alta tensione, ma non sa **quando** farla. A deciderlo è la **centralina** di accensione: sulle moto e sugli scooter più semplici è una scatolina dedicata, spesso chiamata CDI; sulle moto a [iniezione](/motore/iniezione-elettronica/) è la stessa centralina che gestisce anche gli iniettori.

![Schizzo a matita di volano, pick-up, centralina e bobina con una curva di anticipo](/img/motore/centralina-accensione.png)

## Il pick-up: dov'è il pistone?

Sul **volano** (o su una ruota fonica sull'albero motore) c'è un **riferimento**. Accanto, fisso, c'è il **pick-up**: un sensore che, ogni volta che il riferimento gli passa davanti, manda un **impulso** alla centralina.

Da quell'impulso la centralina sa **dove si trova l'albero**, e quindi il pistone, e da quanto in fretta arrivano gli impulsi ricava i **giri** del motore. Per questo un pick-up montato male o guasto può spostare l'accensione o far impazzire il contagiri.

## Quando scoccare: l'anticipo

Come spiegato nel [ciclo a quattro tempi](/motore/il-ciclo-a-quattro-tempi/), la miscela ha bisogno di un po' di tempo per bruciare: la scintilla deve scoccare **prima** che il pistone arrivi al punto morto superiore. Quei gradi di anticipo sono il lavoro della centralina.

- **Anticipo fisso**: la scintilla scocca sempre allo stesso angolo, qualunque siano i giri.
- **Anticipo variabile**: la centralina cambia l'anticipo in base ai **giri**, seguendo una **curva** memorizzata. In generale, salendo di giri serve più anticipo, perché il tempo a disposizione per bruciare la miscela si accorcia.

Le centraline più evolute considerano anche il **carico**: con il gas spalancato e il motore sotto sforzo l'anticipo viene tenuto più basso, per evitare la **detonazione**. Sulle moto a iniezione l'anticipo esce da **mappe** come quelle della benzina, che incrociano giri e carico.

> La forma della curva cambia molto da motore a motore. Nei due tempi da scooter, per esempio, le centraline racing spesso **riducono** l'anticipo agli alti regimi per favorire l'allungo: non vale la regola "più giri, più anticipo" su tutta la curva.

## Il limitatore di giri

Quasi tutte le centraline hanno un **limitatore**: oltre un certo regime tagliano l'accensione per proteggere il motore. Sulle centraline aftermarket la soglia spesso si può regolare, insieme alla scelta tra più curve di anticipo.

## Prima di dare la colpa alla centralina

Quando manca la scintilla o il motore taglia agli alti, la centralina è solo uno dei sospettati. Prima vanno controllati **candela, pipetta, bobina, pick-up, statore, masse e cablaggi**: un guasto in uno qualsiasi di questi pezzi dà sintomi molto simili.

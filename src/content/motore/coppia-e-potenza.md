---
titolo: "Coppia e potenza"
descrizione: "Cosa sono davvero coppia e potenza, come sono legate tra loro e perché il banco prova misura la coppia e calcola i cavalli."
data: 2026-11-12
gruppo: basi
ordine: 4
verificatoIl: 2026-11-12
bozza: false
copertina: /img/motore/coppia-potenza.png
inBreve:
  - "La coppia è la forza con cui l'albero motore fa girare le cose (si misura in Nm)."
  - "La potenza è coppia × velocità di rotazione: kW = Nm × giri/min ÷ 9549."
  - "Il banco prova misura coppia e giri: la potenza si calcola da lì."
  - "Il cambio moltiplica la coppia e riduce i giri; la potenza resta la stessa, a parte le perdite."
glossario:
  - { termine: "Coppia", definizione: "Forza che fa ruotare un albero, moltiplicata per la distanza dall'asse (il braccio). Si misura in newton per metro (Nm)." }
  - { termine: "Potenza", definizione: "Il lavoro fatto nell'unità di tempo. Per un albero che gira è coppia × velocità di rotazione. Si misura in kW o CV." }
  - { termine: "kW e CV", definizione: "Due unità di potenza: 1 kW corrisponde a circa 1,36 CV." }
fonti:
  - { testo: "Zanichelli, Pidatella, «Corso di meccanica», vol. 1, cap. 12 (sintesi)", link: "https://online.scuola.zanichelli.it/pidatellameccanica-files/vol1/sintesi/VOL1_CAP12.pdf" }
  - { testo: "Università di Trieste, lezione «Motori alternativi a combustione interna – calcolo della potenza effettiva»", link: "https://moodle2.units.it/pluginfile.php/207166/mod_resource/content/0/Lezione%203.3.pdf" }
  - { testo: "Motor1, «Coppia e potenza: vi spieghiamo cosa sono»", link: "https://it.motor1.com/news/188806/coppia-e-potenza-vi-spieghiamo-cosa-sono/" }
  - { testo: "Motori Quotidiano, «Come si calcola la potenza di un motore»", link: "https://motori.quotidiano.net/varie/curiosita/motore-come-si-calcola-la-potenza-di-un-motore.htm" }
  - { testo: "Vibromera, «Torque — Power — Speed Calculator» (costante 9549)", link: "https://vibromera.eu/calculators/torque-power-speed" }
  - { testo: "EPI Inc., «Power and Torque»", link: "https://www.epi-eng.com/mechanical_engineering_basics/power_and_torque.htm" }
  - { testo: "Jalopnik, «Bore vs. Stroke: How These Two Specs Decide An Engine's Power»", link: "https://www.jalopnik.com/2037288/bore-vs-stroke-explained/" }
---

Nelle schede tecniche ci sono sempre due numeri: i **cavalli** e i **Nm**. Spesso si dice "la coppia ti spinge, la potenza ti fa andare forte". Ha un fondo di verità, ma il legame tra le due è molto più semplice e preciso di così.

## La coppia: quanto "tira" l'albero

La **coppia** è la forza di rotazione che il motore esercita sull'albero. Se spingi una chiave inglese, la coppia sul bullone è la **forza** che fai per la **lunghezza del braccio**. Si misura in **newton per metro (Nm)**.

Nel motore la forza arriva dai gas che spingono il pistone, e il braccio è la manovella dell'albero motore.

![Schizzo a matita: la coppia come forza per braccio, la potenza come coppia per giri](/img/motore/coppia-potenza.png)

## La potenza: la coppia quando gira

La **potenza** dice quanto lavoro fa il motore in un certo tempo. Per un albero che gira è semplicemente:

**potenza = coppia × velocità di rotazione**

Con le unità che usiamo sulle moto (Nm e giri al minuto) la formula pratica diventa:

**kW = Nm × giri/min ÷ 9549**

Il 9549 non è un numero magico: serve solo a convertire i giri al minuto nell'unità di velocità usata dalla fisica. Per passare ai cavalli: **1 kW ≈ 1,36 CV**.

Un esempio: un motore che dà **100 Nm a 6.000 giri** sviluppa a quel regime 100 × 6.000 ÷ 9549 ≈ **62,8 kW**, cioè circa **85 CV**. Se desse gli stessi 100 Nm a 3.000 giri, la potenza sarebbe la metà: **31,4 kW**.

## Il banco prova misura la coppia

Al banco prova si misurano **coppia e giri**. La curva di potenza si ottiene **moltiplicando punto per punto** la coppia per il regime. Per questo potenza e coppia non sono due "qualità" indipendenti del motore: la potenza **viene dalla coppia**.

Conseguenze pratiche:

- **due motori possono avere la stessa potenza massima con coppie molto diverse**: uno la fa con tanta coppia a pochi giri, l'altro con meno coppia ma girando molto più in alto;
- a parità di coppia, **chi gira più in alto fa più potenza**. È il motivo per cui i motori sportivi cercano i regimi alti, e per cui un motore a corsa corta tende a essere più potente (ne parliamo in [Cilindrata, alesaggio e corsa](/motore/cilindrata-alesaggio-e-corsa/)).

## E il cambio?

Il cambio e la trasmissione finale **moltiplicano la coppia e riducono i giri** (o viceversa). La potenza che passa resta la stessa, a parte le perdite per attrito. È per questo che, in prima, la ruota posteriore riceve molta più coppia di quella che esce dall'albero motore.

> "Coppia" e "potenza" non sono in competizione. La coppia dice quanto spinge il motore a un certo regime. La potenza dice quanto lavoro fa, ed è la coppia moltiplicata per la velocità con cui gira.

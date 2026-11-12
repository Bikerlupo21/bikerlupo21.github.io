---
titolo: "Iniezione elettronica"
descrizione: "Sensori, centralina, mappe e iniettori: come l'iniezione elettronica decide quanta benzina dare, cos'è la sonda lambda e da dove arriva l'effetto on-off."
data: 2026-11-12
gruppo: alimentazione
ordine: 2
verificatoIl: 2026-11-12
bozza: false
copertina: /img/motore/iniezione-schema.png
inBreve:
  - "La centralina legge i sensori e, dalle mappe, decide per quanto tempo tenere aperto l'iniettore."
  - "La benzina arriva all'iniettore in pressione, spinta da una pompa elettrica."
  - "Con la sonda lambda la centralina controlla il risultato e corregge, ma solo in certe condizioni."
glossario:
  - { termine: "ECU", definizione: "La centralina elettronica che gestisce iniezione e accensione." }
  - { termine: "Mappa", definizione: "Una tabella nella centralina: per ogni combinazione di giri e carico dice quanta benzina e quanto anticipo." }
  - { termine: "Tempo di iniezione", definizione: "Per quanto l'iniettore resta aperto a ogni ciclo: è così che si dosa la benzina." }
  - { termine: "TPS", definizione: "Sensore di posizione della farfalla." }
  - { termine: "MAP", definizione: "Sensore della pressione nel condotto di aspirazione." }
  - { termine: "Sonda lambda", definizione: "Sensore nello scarico che misura l'ossigeno rimasto e dice se la miscela è grassa o magra." }
fonti:
  - { testo: "Moto.it, «L'alimentazione a iniezione sulle moto a 4 tempi»" }
  - { testo: "InSella, «Effetto on-off del motore: cause e rimedi»", link: "https://www.insella.it/da-sapere/tecnica/effetto-on-off-del-motore-cause-rimedi-un-problema-fastidioso-62215" }
  - { testo: "Bosch, documentazione tecnica Motronic (sensori, mappe, tempo di iniezione)" }
  - { testo: "Hella, informazioni tecniche sugli iniettori" }
  - { testo: "Brevetto US 5.174.263, sistema di gestione motore per motocicli" }
  - { testo: "Motofomo, ciclo aperto e ciclo chiuso nelle moto a iniezione" }
  - { testo: "Bikeboy.org, iniezione e rapporto aria/benzina" }
  - { testo: "MoTeC, manuali delle centraline (mappe carburante e accensione)" }
---

Con l'iniezione elettronica la benzina non viene più "aspirata" come nel [carburatore](/motore/carburatore/): viene **spruzzata in pressione** da un iniettore, e a decidere quanta è una **centralina**.

![Schizzo a matita dello schema dell'iniezione: sensori, centralina, iniettore e pompa](/img/motore/iniezione-schema.png)

## I pezzi

- La **pompa elettrica** spinge la benzina dal serbatoio e la tiene **in pressione** fino agli iniettori.
- L'**iniettore** è una valvola **elettromagnetica**: quando la centralina gli dà corrente si apre e spruzza benzina nebulizzata nel condotto di aspirazione; quando toglie corrente si chiude.
- La **centralina** (ECU) è il cervello: legge i sensori e comanda iniettori e accensione.
- Il [corpo farfallato](/motore/corpo-farfallato/) regola l'aria: qui passa solo aria, la benzina la mette l'iniettore.

## Cosa legge la centralina

I sensori principali sono:

- **posizione della farfalla** (TPS): quanto stai aprendo il gas;
- **pressione nel condotto di aspirazione** (MAP): quanto il motore sta "tirando";
- **temperatura dell'aria** e **temperatura del motore**;
- **giri e posizione dell'albero motore**.

## Le mappe

Dentro la centralina ci sono delle **mappe**: tabelle che, per ogni combinazione di **giri** e **carico** (dato dall'apertura della farfalla o dalla pressione in aspirazione), indicano quanta benzina iniettare e quanto **anticipo di accensione** dare.

La benzina si dosa con il **tempo di iniezione**: la pressione è costante, quindi più a lungo l'iniettore resta aperto, più benzina entra.

Poi ci sono le **correzioni**: a motore **freddo** la centralina arricchisce la miscela, e lo fa anche quando **apri il gas di colpo**, come la pompa di ripresa del carburatore.

## La sonda lambda: ciclo chiuso e ciclo aperto

Nello scarico c'è la **sonda lambda**, che misura l'ossigeno rimasto nei gas e dice se la miscela era grassa o magra.

- **Ciclo chiuso**: in andatura costante la centralina legge la sonda e corregge di continuo, tenendo la miscela vicina al rapporto stechiometrico. Serve soprattutto a far lavorare bene il **catalizzatore**.
- **Ciclo aperto**: al **minimo**, in **accelerazione** e a **pieno carico** la centralina ignora la sonda e usa solo le mappe, che lì chiedono una miscela diversa.

## L'effetto on-off

Su alcune moto a iniezione la risposta alle **piccole aperture** del gas è brusca: il motore passa da "niente" a "tira" come un interruttore. Le cause possibili sono diverse: mappe molto magre in quella zona, un sensore di posizione farfalla regolato male o, sui pluricilindrici, **corpi farfallati non sincronizzati**. Le case l'hanno ridotto molto con sensori più precisi, mappe più raffinate e il ride-by-wire.

> Quando e quanto la centralina usi la sonda lambda cambia da moto a moto: lo schema ciclo chiuso / ciclo aperto descritto qui è quello generale.

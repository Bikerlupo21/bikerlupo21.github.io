---
titolo: "Corpo farfallato"
descrizione: "La valvola che decide quanta aria entra nel motore: com'è fatto il corpo farfallato, la differenza tra comando a cavo e ride-by-wire e perché sui pluricilindrici va sincronizzato."
data: 2026-11-12
gruppo: alimentazione
ordine: 3
verificatoIl: 2026-11-12
bozza: false
copertina: /img/motore/corpo-farfallato.png
inBreve:
  - "Il corpo farfallato regola l'aria che entra nel motore: con l'iniezione, la benzina la mette l'iniettore."
  - "A cavo la manopola muove direttamente la farfalla; col ride-by-wire la muove un motorino comandato dalla centralina."
  - "Il ride-by-wire ha reso possibili riding mode e controlli elettronici dell'erogazione."
glossario:
  - { termine: "Farfalla", definizione: "Il disco che ruota dentro il condotto: chiuso lascia passare pochissima aria, di taglio la lascia passare tutta." }
  - { termine: "TPS", definizione: "Sensore che comunica alla centralina la posizione della farfalla." }
  - { termine: "Ride-by-wire", definizione: "Acceleratore elettronico: la manopola manda un segnale, la farfalla la muove un attuatore." }
  - { termine: "Sincronizzazione", definizione: "Regolazione che fa aprire insieme i corpi farfallati dei vari cilindri." }
fonti:
  - { testo: "Hella, «Informazioni tecniche: corpo farfallato» (PDF)", link: "https://www.hella.com/tibi/ti/it/electronics/ti_ita_electronics_drosselklappenstutzen.pdf" }
  - { testo: "alVolante, «Cos'è e come funziona il corpo farfallato»", link: "https://www.alvolante.it/da_sapere/tecnica/motori/cos-e-e-come-funziona-il-corpo-farfallato-408933" }
  - { testo: "InSella, «Elettronica sulle moto: come funziona la piattaforma inerziale» (ride-by-wire)", link: "https://www.insella.it/news/elettronica-sulle-moto-come-funziona-piattaforma-inerziale" }
  - { testo: "Quotidiano Motori, «Elettronica: come funziona sulle moto»", link: "https://motori.quotidiano.net/?p=259370" }
  - { testo: "Motoclub Tingavert, elettronica sulle moto (ride-by-wire e riding mode)", link: "https://www.motoclub-tingavert.it/a3553s.html" }
  - { testo: "KTM, «Riding mode e selezione delle mappature del motore»", link: "https://www.ktm.com/it-ch/tech-guide/engine-map-selection.html" }
  - { testo: "Ducati Diavel, manuale d'officina: introduzione al sistema di controllo motore", link: "https://www.manualslib.com/manual/834200/Ducati-Diavel.html?page=266" }
  - { testo: "InSella, «Effetto on-off del motore: cause e rimedi» (sincronizzazione)", link: "https://www.insella.it/da-sapere/tecnica/effetto-on-off-del-motore-cause-rimedi-un-problema-fastidioso-62215" }
  - { testo: "Hot n' Rare, manuale STVE (farfalla secondaria comandata dalla centralina, PDF)", link: "https://www.hotnrare.com/pdf/STVE_Manual_it.pdf" }
---

Nelle moto a [iniezione](/motore/iniezione-elettronica/) il carburatore non c'è più: al suo posto c'è il **corpo farfallato**. È un pezzo di condotto con dentro una **valvola a farfalla**, e il suo lavoro è uno solo: **regolare quanta aria entra nel motore**.

![Schizzo a matita del comando a cavo e del ride-by-wire](/img/motore/corpo-farfallato.png)

## Com'è fatto

- La **farfalla** è un disco montato su un alberino. Chiusa, lascia passare pochissima aria; girata di taglio, apre tutto il condotto.
- Un **sensore di posizione** (TPS) dice alla centralina quanto è aperta la farfalla. È uno dei dati principali per decidere quanta benzina iniettare.
- Spesso sul corpo farfallato è montato anche l'**iniettore**.

Con l'iniezione nel corpo farfallato passa **solo aria**: la benzina la aggiunge l'iniettore, dosata dalla centralina.

## Comando a cavo

È il sistema classico, ancora diffuso su tante moto e scooter: la manopola tira un **cavo** che fa ruotare la farfalla. A ogni movimento del polso corrisponde un movimento uguale della farfalla.

## Ride-by-wire

Con il **ride-by-wire** (acceleratore elettronico) il cavo verso la farfalla sparisce:

1. un **sensore** sulla manopola legge quanto stai girando il gas;
2. la **centralina** riceve il segnale e decide quanto aprire la farfalla;
3. un **motorino elettrico** sul corpo farfallato la muove, e un sensore ne controlla la posizione.

La rotazione della manopola, quindi, è una **richiesta**: la farfalla la apre la centralina. È questo che ha reso possibili i **riding mode**, che cambiano la risposta al gas e la potenza disponibile, e controlli come quello di **trazione**, che lavorano insieme alla gestione della farfalla.

Prima del ride-by-wire completo alcune moto usavano un sistema a **doppia farfalla**: una comandata dal cavo, l'altra (secondaria) mossa da un attuatore comandato dalla centralina.

## Più cilindri, più corpi farfallati

Sui pluricilindrici di solito c'è un corpo farfallato per cilindro, collegati tra loro. Devono aprirsi **tutti insieme**: se non sono **sincronizzati**, ogni cilindro riceve un'aria diversa e il motore gira irregolare, soprattutto al minimo e alle piccole aperture.

## Manutenzione

Di regola il corpo farfallato non chiede interventi particolari, ma con il tempo può **sporcarsi** con residui d'olio e vapori. Spesso basta una pulizia; se si guasta il sensore di posizione o l'attuatore elettrico, il pezzo va sostituito.

> Sincronizzazione e pulizia vanno fatte con la procedura del manuale d'officina: su alcuni corpi farfallati elettronici dopo l'intervento serve una procedura di apprendimento con lo strumento di diagnosi.

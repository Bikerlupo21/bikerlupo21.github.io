---
titolo: "Fasatura"
descrizione: "Quando si aprono e si chiudono le valvole rispetto al pistone: anticipi, ritardi, incrocio, diagramma della distribuzione e fasatura variabile."
data: 2026-11-12
gruppo: distribuzione
ordine: 4
verificatoIl: 2026-11-12
bozza: false
copertina: /img/motore/fasatura-diagramma.png
inBreve:
  - "Le valvole non aprono e chiudono ai punti morti: aprono prima e chiudono dopo."
  - "Così si sfrutta l'inerzia dei gas e il cilindro si riempie e si svuota meglio."
  - "L'incrocio è il momento, attorno al PMS, in cui aspirazione e scarico sono aperti insieme."
  - "La fasatura si esprime in gradi di rotazione dell'albero motore e cambia molto il carattere del motore."
glossario:
  - { termine: "Fasatura", definizione: "I momenti di apertura e chiusura delle valvole rispetto alla posizione dell'albero motore." }
  - { termine: "Anticipo di apertura", definizione: "Di quanti gradi una valvola inizia ad aprirsi prima del punto morto." }
  - { termine: "Ritardo di chiusura", definizione: "Di quanti gradi una valvola finisce di chiudersi dopo il punto morto." }
  - { termine: "Incrocio", definizione: "Il periodo attorno al PMS in cui la valvola di scarico non ha finito di chiudersi e quella di aspirazione ha già iniziato ad aprirsi." }
  - { termine: "Diagramma della distribuzione", definizione: "Il disegno che mostra in gradi i punti di apertura e chiusura delle valvole." }
fonti:
  - { testo: "Motor1, «La fasatura variabile»", link: "https://it.motor1.com/news/199722/la-fasatura-variabile/" }
  - { testo: "Wikipedia, «Valve timing»", link: "https://en.wikipedia.org/wiki/Valve_timing" }
  - { testo: "Moto.it, «Le fasi e le alzate della distribuzione»", link: "https://www.moto.it/news/le-fasi-e-le-alzate-della-distribuzione.html" }
  - { testo: "Moto.it, «Camme, fasi e cavalli (prima parte)»", link: "https://www.moto.it/news/camme-fasi-e-cavalli-prima-parte.html" }
  - { testo: "Moto.it, «Camme, fasi e cavalli (seconda parte)»", link: "https://www.moto.it/news/camme-fasi-e-cavalli-seconda-parte.html" }
  - { testo: "Automoto.it, «Cosa è l'incrocio»", link: "https://www.automoto.it/news/cosa-e-l-incrocio.html" }
  - { testo: "Moto.it, «Le distribuzioni a fasatura variabile: più prestazioni e meno emissioni»", link: "https://www.moto.it/news/le-distribuzioni-a-fasatura-variabile-piu-prestazioni-e-meno-emissioni.html" }
  - { testo: "Scribd, «Valve Timing Diagrams» (dispensa)", link: "https://www.scribd.com/doc/271475962/Valve-Timing-Diagrams" }
  - { testo: "CarBikeTech, «Engine Valve Timing Explained»", link: "https://carbiketech.com/?p=5997" }
  - { testo: "Motoclub Tingavert, «I diagrammi di distribuzione»", link: "https://www.motoclub-tingavert.it/a330s.html" }
  - { testo: "Vivid Racing, «Valves» (effetto del gioco sulla fasatura)", link: "https://www.vividracing.com/valves-c-9871.html" }
---

Nel [ciclo a quattro tempi](/motore/il-ciclo-a-quattro-tempi/) si dice per semplicità che le valvole aprono e chiudono ai punti morti. Nei motori veri non è così, ed è proprio lì che si nasconde una buona parte delle prestazioni: nella **fasatura**.

## Cos'è

La fasatura indica **quando** si aprono e si chiudono le valvole di aspirazione e di scarico **rispetto alla posizione dell'albero motore** e quindi del pistone. Si esprime in **gradi di rotazione dell'albero motore**: di quanti gradi la valvola apre **prima** del punto morto (**anticipo**) e di quanti gradi chiude **dopo** (**ritardo**).

![Schizzo a matita del diagramma della distribuzione con anticipi, ritardi e incrocio](/img/motore/fasatura-diagramma.png)

## Perché aprire prima e chiudere dopo

Le valvole non si aprono di colpo: la camma le solleva gradualmente. E i gas hanno una massa, quindi un'**inerzia**.

- **L'aspirazione apre prima del PMS** così che, quando il pistone inizia a scendere, la valvola sia già ben aperta.
- **L'aspirazione chiude dopo il PMI**: la miscela che sta entrando ha slancio e continua a riempire il cilindro anche quando il pistone ha già iniziato a risalire. Questo ritardo di chiusura è uno dei valori più importanti per le prestazioni.
- **Lo scarico apre prima del PMI**: una parte dei gas, ancora in pressione, esce da sola, e il pistone fa meno fatica a spingere fuori il resto.
- **Lo scarico chiude dopo il PMS**, sfruttando la velocità dei gas in uscita.

La durata di ogni fase è quindi **180° + anticipo + ritardo**: più di mezzo giro.

## L'incrocio

Attorno al PMS, tra la fine dello scarico e l'inizio dell'aspirazione, ci sono alcuni gradi in cui **le due valvole sono aperte insieme**: è l'**incrocio**. Dura quanto l'anticipo di apertura dell'aspirazione più il ritardo di chiusura dello scarico. I gas di scarico che escono veloci aiutano a richiamare la miscela fresca e a "lavare" il cilindro.

Ma l'incrocio ha un prezzo:

- un **incrocio ampio** aiuta ai regimi alti, ed è tipico dei motori da corsa;
- ai **bassi regimi e al minimo** mescola gas freschi e combusti, rende il funzionamento irregolare e peggiora le emissioni. Per questo i motori stradali ne hanno meno.

## Messa in fase

Al montaggio la distribuzione va **messa in fase**, cioè l'albero a camme va posizionato nel modo giusto rispetto all'albero motore. Sui motori di serie ci sono dei **segni di riferimento**. Per lavori di precisione si usano un **disco goniometrico** e dei **comparatori**, per verificare i gradi di apertura e chiusura indicati dal costruttore.

Anche il **gioco valvole** conta: se è troppo grande, la valvola apre più tardi e chiude prima, e la fasatura reale non è più quella di progetto.

## Fasatura variabile

Con una fasatura fissa bisogna scegliere un compromesso tra regimi bassi e alti. I sistemi a **fasatura variabile** ruotano l'albero a camme rispetto alla sua ruota dentata mentre il motore gira: la durata della fase resta la stessa, ma cambiano anticipi e ritardi, e quindi l'incrocio. Così si può avere un minimo regolare e insieme potenza in alto.

> I gradi di fasatura cambiano da motore a motore: non esiste un valore "giusto" in assoluto. Lo schema qui sopra è solo qualitativo.

---
titolo: "Bobina"
descrizione: "Come la bobina trasforma i 12 volt della batteria nelle decine di migliaia di volt che servono alla candela: primario, secondario, accensione induttiva e a scarica capacitiva (CDI)."
data: 2026-11-12
gruppo: accensione
ordine: 2
verificatoIl: 2026-11-12
bozza: false
copertina: /img/motore/bobina-schema.png
inBreve:
  - "La bobina è un trasformatore: poche spire nel primario, moltissime nel secondario."
  - "Quando la corrente nel primario si interrompe di colpo, nel secondario nasce l'alta tensione per la candela."
  - "Con la CDI invece è un condensatore carico a scaricarsi di colpo nel primario."
glossario:
  - { termine: "Primario", definizione: "L'avvolgimento con poche spire di filo grosso, collegato a batteria e centralina." }
  - { termine: "Secondario", definizione: "L'avvolgimento con moltissime spire di filo sottile, collegato alla candela." }
  - { termine: "Accensione induttiva (TCI)", definizione: "La bobina accumula energia come campo magnetico; un transistor interrompe la corrente e fa scoccare la scintilla." }
  - { termine: "CDI", definizione: "Accensione a scarica capacitiva: un condensatore carico si scarica nel primario della bobina." }
  - { termine: "Scintilla persa", definizione: "Sistema in cui una bobina accende insieme due candele: una in compressione, l'altra in scarico." }
fonti:
  - { testo: "Bosch, «Bobine d'accensione» (PDF)", link: "https://www.boschaftermarket.com/xrm/media/images/country_specific/it/xx_pdfs_28/parts_5/bobine.pdf" }
  - { testo: "Motori Magazine, «Accensione: cosa è la bobina d'accensione»", link: "https://www.motorimagazine.it/accensione-cosa-la-bobbina-daccensione/" }
  - { testo: "Motori Magazine, «Accensione: come funziona nei sistemi elettronici»", link: "https://www.motorimagazine.it/accensione-funziona-nei-sistemi-elettronici/" }
  - { testo: "UTI, «Motorcycle Ignition Systems: What Are They and How Do They Work?»", link: "https://uti.edu/blog/motorcycle/motorcycle-ignition-systems" }
  - { testo: "Cycle World (1969), «Understanding electronic ignition»", link: "https://magazine.cycleworld.com/article/1969/11/1/understanding-electronic-ignition" }
  - { testo: "Shindengen, «Ignition Unit (TCI and CDI Systems)»", link: "https://shindengen.com/products/electro/motorcycle/dccdi" }
  - { testo: "Old Skool Suzuki, «Ignition components»", link: "https://oldskoolsuzuki.info/archives/category/ross-farnham" }
  - { testo: "TEXA Edu, sistemi di accensione (PDF)", link: "https://www.texa.it/wp-content/uploads/2021/02/texaedu-g3c-it.pdf" }
  - { testo: "alVolante, «Spinterogeno: a cosa serve, come funziona»", link: "https://www.alvolante.it/da_sapere/tecnica/elettronica-e-software/spinterogeno-cosa-serve-come-funziona-tipi-e-cosa-e-stato-sostituito-379955" }
  - { testo: "RevZilla, «What is wasted-spark ignition, and do I want it?»", link: "https://www.revzilla.com/common-tread/wtatwta-what-is-wasted-spark-ignition-and-do-i-want-it" }
  - { testo: "Dynatek, FAQ accensioni single fire e dual fire", link: "https://www.motorcycleid.com/dynatek/info/faq.html" }
  - { testo: "SicurAUTO, «Test bobine di accensione: come verificare il funzionamento»", link: "https://www.sicurauto.it/ricambi-e-accessori/tecnica-e-manutenzione/test-bobine-di-accensione-come-verificare-il-funzionamento/" }
---

La [candela](/motore/candela/) per far scoccare la scintilla ha bisogno di **decine di migliaia di volt**. La batteria ne dà 12. A colmare la differenza ci pensa la **bobina**.

![Schizzo a matita della bobina con primario, secondario e nucleo](/img/motore/bobina-schema.png)

## Com'è fatta

La bobina è un **trasformatore**: due avvolgimenti di filo intorno a un **nucleo di ferro**.

- Il **primario** ha **poche spire** di filo più grosso ed è collegato all'impianto (batteria e centralina).
- Il **secondario** ha **moltissime spire** di filo sottile, indicativamente un centinaio di volte quelle del primario, ed è collegato alla candela.

## Come nasce l'alta tensione

Nell'accensione **induttiva** (sulle moto si parla spesso di TCI, accensione a transistor):

1. la corrente passa nel primario e crea un **campo magnetico**, in cui la bobina accumula energia;
2. al momento giusto la centralina **interrompe di colpo** la corrente;
3. il campo magnetico crolla e nel secondario, che ha molte più spire, si genera un impulso ad **alta tensione**;
4. l'alta tensione arriva alla candela e scocca la scintilla.

Più veloce è il crollo del campo, più forte è l'impulso. Sulle moto vecchie a interrompere la corrente erano le **puntine platinate** del ruttore, con un condensatore in parallelo; oggi lo fa un **transistor** nella centralina, che non si consuma.

## L'accensione CDI

Molte moto, scooter e fuoristrada usano la **CDI** (accensione a scarica capacitiva). Qui un **condensatore** viene caricato a qualche centinaio di volt e, al momento dell'accensione, si **scarica tutto insieme** nel primario della bobina. Il secondario alza ancora la tensione fino a quella che serve alla candela.

Il vantaggio è che la bobina si "carica" molto più in fretta: utile sui motori che girano molto in alto.

## Bobine, cavi e pipette

- Nei sistemi classici la bobina è separata e l'alta tensione arriva alla candela con un **cavo** e una **pipetta**.
- Su tanti motori moderni c'è una **bobina per ogni candela**, spesso montata **direttamente sopra la candela** (bobina "a matita"): niente cavi ad alta tensione e meno possibilità di dispersioni.
- Nella pipetta o nella bobina c'è di solito una **resistenza antidisturbo**, che limita le interferenze elettriche.

## La scintilla persa

Su molti bicilindrici, soprattutto del passato, **una sola bobina accende due candele insieme**. Una delle due scocca nel cilindro in compressione e fa il suo lavoro; l'altra scocca nel cilindro che sta scaricando, dove non c'è niente da accendere: è la **scintilla persa** (*wasted spark*). Semplifica l'impianto, ma l'anticipo non si può regolare separatamente per i due cilindri.

> Si può controllare una bobina misurando la resistenza del primario (bassa, pochi ohm) e del secondario (migliaia di ohm), ma i valori cambiano molto da bobina a bobina: quelli giusti sono nel manuale d'officina.

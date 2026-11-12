import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// Campi comuni a tutti gli articoli
// Riferimento a un altro contenuto: accetta sia "nome-file" sia il percorso completo
// (es. "src/content/brand/nome-file.md", come lo salva il pannello Pages CMS).
const rif = z.string().transform((v) => v.replace(/^.*\//, '').replace(/\.mdx?$/, ''));

// Il pannello può salvare campi vuoti come "" o null: li trattiamo come "non compilato".
const vuoto = (v: unknown) => (v === '' || v === null ? undefined : v);
const opz = <T extends z.ZodTypeAny>(t: T) => z.preprocess(vuoto, t.optional());
const lista = <T extends z.ZodTypeAny>(t: T) => z.preprocess(vuoto, z.array(t).default([]));

const base = {
  titolo: z.string(),
  descrizione: z.string(),
  data: z.coerce.date(),
  bozza: z.preprocess(vuoto, z.boolean().default(false)), // true = visibile solo in locale, non pubblicato
  copertina: opz(z.string()), // percorso in /public, es. /img/articoli/foto.jpg
  brand: lista(rif),
};

const pezzo = z.object({
  cosa: z.string(),
  brand: opz(z.string()),
  costo: opz(z.string()),
  link: opz(z.string().url()),
});

// Dal video + Provato da me
const articoli = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articoli' }),
  schema: z.object({
    ...base,
    rubrica: z.enum(['dal-video', 'provato-da-me']),
    youtube: opz(z.string()), // solo l'ID del video, es. dQw4w9WgXcQ
    capitoli: lista(z.object({ tempo: z.string(), titolo: z.string() })),
    pezzi: lista(pezzo),
    totale: opz(z.string()),
    voto: opz(z.string()), // per "Provato da me", es. "8/10"
    pro: lista(z.string()),
    contro: lista(z.string()),
  }),
});

// Pagina madre di un progetto
const progetti = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/progetti' }),
  schema: z.object({
    titolo: z.string(),
    descrizione: z.string(),
    moto: z.string(),
    puntatePreviste: z.number().int().positive(),
    stato: z.enum(['in-corso', 'concluso']).default('in-corso'),
    spesaTotale: opz(z.string()),
    copertina: opz(z.string()),
    data: z.coerce.date(),
    bozza: z.preprocess(vuoto, z.boolean().default(false)),
  }),
});

// Le singole puntate di un progetto
const puntate = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/puntate' }),
  schema: z.object({
    ...base,
    progetto: rif,
    numero: z.number().int().positive(),
    youtube: opz(z.string()),
    tempo: opz(z.string()),
    costo: opz(z.string()),
    difficolta: opz(z.number().int().min(1).max(5)),
    ricambi: lista(pezzo),
  }),
});

// Il motore: articoli verificati
const motore = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/motore' }),
  schema: z.object({
    ...base,
    gruppo: z.enum([
      'basi', 'manovellismo', 'distribuzione', 'alimentazione',
      'accensione', 'lubrificazione-raffreddamento', 'trasmissione', 'scarico',
    ]),
    ordine: z.number().int(),
    verificatoIl: z.coerce.date(),
    inBreve: z.array(z.string()).min(1),
    glossario: lista(z.object({ termine: z.string(), definizione: z.string() })),
    // Regola: nessun articolo del motore senza almeno 2 fonti.
    fonti: z.array(z.object({ testo: z.string(), link: opz(z.string().url()) })).min(2),
    correzioni: lista(z.object({ data: z.coerce.date(), testo: z.string() })),
    youtube: opz(z.string()),
  }),
});

const brand = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/brand' }),
  schema: z.object({
    nome: z.string(),
    categoria: z.enum(['Abbigliamento', 'Accessori', 'Ricambi', 'Pneumatici', 'Moto', 'Elettronica', 'Caschi', 'Pista', 'Community']),
    giudizio: opz(z.string()),
    miPiace: opz(z.string()),
    nonMiPiace: opz(z.string()),
    provato: lista(z.string()),
    sito: opz(z.string().url()),
    bozza: z.preprocess(vuoto, z.boolean().default(false)),
  }),
});

export const collections = { articoli, progetti, puntate, motore, brand };

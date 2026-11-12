import { getCollection, type CollectionEntry } from 'astro:content';

// In produzione le bozze non escono mai; in locale (npm run dev) le vedi.
const mostraBozze = import.meta.env.DEV || import.meta.env.PUBLIC_MOSTRA_BOZZE === 'true';
export const visibile = ({ data }: { data: { bozza?: boolean } }) => mostraBozze || !data.bozza;

export const perData = <T extends { data: { data: Date } }>(a: T, b: T) =>
  b.data.data.valueOf() - a.data.data.valueOf();

export async function articoli() {
  return (await getCollection('articoli', visibile)).sort(perData);
}
export async function puntate() {
  return (await getCollection('puntate', visibile)).sort(perData);
}
export async function motore() {
  return (await getCollection('motore', visibile)).sort((a, b) => a.data.ordine - b.data.ordine);
}

export async function progetti() {
  return (await getCollection('progetti', visibile)).sort(perData);
}
export async function brand() {
  return (await getCollection('brand', visibile)).sort((a, b) => a.data.nome.localeCompare(b.data.nome, 'it'));
}

export const RUBRICHE = {
  'dal-video': 'Dal video',
  'provato-da-me': 'Provato da me',
} as const;

export const GRUPPI_MOTORE: { id: CollectionEntry<'motore'>['data']['gruppo']; nome: string; componenti: string[] }[] = [
  { id: 'basi', nome: 'Le basi', componenti: ['Il ciclo a quattro tempi', 'Il ciclo a due tempi', 'Cilindrata, alesaggio e corsa', 'Coppia e potenza'] },
  { id: 'manovellismo', nome: 'Manovellismo', componenti: ['Pistone e fasce', 'Biella', 'Albero motore', 'Cilindro e testata'] },
  { id: 'distribuzione', nome: 'Distribuzione', componenti: ['Valvole', 'Alberi a camme', 'Catena o cinghia', 'Fasatura'] },
  { id: 'alimentazione', nome: 'Alimentazione', componenti: ['Carburatore', 'Iniezione elettronica', 'Corpo farfallato', 'Airbox e filtro'] },
  { id: 'accensione', nome: 'Accensione', componenti: ['Candela', 'Bobina', 'Centralina'] },
  { id: 'lubrificazione-raffreddamento', nome: 'Lubrificazione e raffreddamento', componenti: ['Olio e pompa', 'Raffreddamento ad aria', 'Raffreddamento a liquido'] },
  { id: 'trasmissione', nome: 'Trasmissione', componenti: ['Frizione', 'Cambio', 'Trasmissione finale'] },
  { id: 'scarico', nome: 'Scarico', componenti: ['Collettori', 'Catalizzatore', 'Silenziatore'] },
];

export const fmtData = (d: Date) =>
  d.toLocaleDateString('it-IT', { day: 'numeric', month: 'long', year: 'numeric' });

export const minLettura = (testo = '') => Math.max(1, Math.round(testo.split(/\s+/).length / 200));

// Link e etichetta di qualsiasi contenuto, per elenchi misti (es. scheda brand)
export function info(e: CollectionEntry<'articoli' | 'puntate' | 'motore'>) {
  if (e.collection === 'articoli') return { href: `/articoli/${e.id}/`, tag: RUBRICHE[e.data.rubrica] };
  if (e.collection === 'puntate') return { href: `/progetti/${e.data.progetto}/${e.id}/`, tag: `Progetti · Puntata ${e.data.numero}` };
  return { href: `/motore/${e.id}/`, tag: 'Il motore' };
}

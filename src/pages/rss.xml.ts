import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { articoli, puntate, motore, info } from '../lib/dati';
import { SITO } from '../lib/sito';

export async function GET(context: APIContext) {
  const voci = [...(await articoli()), ...(await puntate()), ...(await motore())]
    .sort((a, b) => b.data.data.valueOf() - a.data.data.valueOf());
  return rss({
    title: SITO.nome,
    description: SITO.descrizione,
    site: context.site!,
    items: voci.map((v) => ({
      title: v.data.titolo,
      description: v.data.descrizione,
      pubDate: v.data.data,
      link: info(v).href,
    })),
    customData: '<language>it-it</language>',
  });
}

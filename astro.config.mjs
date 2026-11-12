// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Quando avrai il dominio, cambia questo indirizzo (serve per sitemap, RSS e anteprime social).
export default defineConfig({
  site: 'https://bikerlupo21.github.io',
  integrations: [sitemap()],
  trailingSlash: 'ignore',
});

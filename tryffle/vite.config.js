import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  build: {
    manifest: true,
    outDir: 'tryffle/static/dist',
    rollupOptions: {
      input: 'tryffle/static/js/main.js', // Chemin mis à jour
    },
  },
  server: {
    proxy: {
      '/': 'http://127.0.0.1:8000',
    },
  },
});

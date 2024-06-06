import { defineConfig } from "vite";
import { resolve } from "path";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  root: resolve("/app/static/src"),
  base: "/app/static/",
  plugins: [vue()],
  build: {
    outDir: resolve("/app/static/manifest.json"),
    assetsDir: "",
    manifest: true,
    emptyOutDir: true,
    rollupOptions: {
      // Overwrite default .html entry to main.ts in the static directory
      input:{
        main: resolve("/app/static/src/js/main.js"),
      } 
    },
  },
});
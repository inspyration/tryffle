import "vite/modulepreload-polyfill";
import { createApp, h } from "vue";
import { createInertiaApp } from "@inertiajs/vue3";
import "../index.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';

createInertiaApp({
  resolve: (name) => import(`./pages/${name}.vue`),
  setup({ el, App, props, plugin }) {
    createApp({ render: () => h(App, props) })
      .use(plugin)
      .mount(el);
  },
});
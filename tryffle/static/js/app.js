import { createApp, h } from 'vue';
import { createInertiaApp } from '@inertiajs/inertia-vue3';
import DefaultLayout from './Layouts/DefaultLayout.vue';



createInertiaApp({
    resolve: (name) => import(`./Pages/${name}.vue`),
    setup({ el, App, props, plugin }) {
      createApp({ render: () => h(App, props) })
        .use(plugin)
        .mount(el);
    },
  });

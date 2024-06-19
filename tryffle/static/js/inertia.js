import { createInertiaApp } from '@inertiajs/inertia-vue'

createInertiaApp({
    resolve: name => require(`./Pages/${name}`),
})

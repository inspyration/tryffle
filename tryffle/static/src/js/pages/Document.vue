<template lang="">
    <div>
        <h1>Voici la liste de tous les documents enregistrés</h1>
        <div v-for="doc in documents" :key="index">
            <h2> {{doc.title}} </h2>
            <a :href="`${doc.id}/`">Cliquer pour plus de détails concernant les pages de ce documents</a>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        documents : {
            type: Array,
            required: true
        }
    }
}
</script>
<style lang="">
    
</style>
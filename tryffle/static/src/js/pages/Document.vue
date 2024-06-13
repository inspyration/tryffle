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
    data() {
        return {
            documents: []
        };
    },
    mounted(){
        this.getDocuments();
    },
    methods: {
        getDocuments() {
            fetch('http://localhost:8000/api/v1/documents/')
            .then(response => {
                if(!response.ok){
                    throw new Error("Error response");
                }
                return response.json();
            })
            .then(data => {
                this.documents = data;
            })
            .catch(error => {
                console.error('Erreur lors de la récupération des documents:', error);
            });
        }
    }
};
</script>
<style lang="">
    
</style>
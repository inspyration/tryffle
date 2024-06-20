<template lang="">
    <div>
        <h1 class="text-blue-500">Voici la liste de tous les documents enregistrés</h1>
        <div v-for="(doc, index) in documents" :key="index" class="card mb-3">
      <div class="card-body">
        <h2 class="card-title">{{ doc.title }}</h2>
        <a :href="`${doc.id}/`" class="btn btn-primary">Cliquer pour plus de détails concernant les pages de ce document</a>
      </div>
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
<template lang="">
    <div class="container mt-5">
      <h1 class="text-primary mb-4">Voici les informations du document : {{ document.title }}</h1>
      <h3 class="mb-3">Date d'ajout du document : <span class="text-secondary">{{ document.date }}</span></h3>
      <h3 class="mb-3">Ce document possède {{ document.page_number }} pages :</h3>
      <ul class="list-group">
        <li v-for="page in pages" :key="page.number" class="list-group-item">
          <a :href="`page/${page.number}/`" class="text-decoration-none text-info">Page {{ page.number }}</a>
        </li>
      </ul>
    </div>
  </template>
<script>
export default {
  props: {
    documentId: {
      type: Number,
      required: true
    }
  },
  data() {
        return {
            pages: [],
            document: []
        };
    },
    mounted(){
        this.getPages();
        this.getDocument();
    },
    methods: {
        getPages() {
            fetch(`http://localhost:8000/api/v1/documents/${this.documentId}/pages/`)
            .then(response => {
                if(!response.ok){
                    throw new Error("Error response");
                }
                return response.json();
            })
            .then(data => {
                this.pages = data;
            })
            .catch(error => {
                console.error('Erreur lors de la récupération des documents:', error);
            });
        },

        getDocument() {
            fetch(`http://localhost:8000/api/v1/documents/${this.documentId}`)
            .then(response => {
                if(!response.ok){
                    throw new Error("Error response");
                }
                return response.json();
            })
            .then(data => {
                this.document = data;
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
<template lang="">
    <div>
        <h1>Test {{documentId}}</h1>
        <ul>
          <li v-for="page in pages" :key="page.number">
            <a :href="`page/${page.number}/`">Page {{ page.number }}</a>
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
            pages: []
        };
    },
    mounted(){
        this.getPages();
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
        }
    }
};
</script>
<style lang="">
    
</style>
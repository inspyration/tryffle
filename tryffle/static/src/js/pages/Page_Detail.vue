<template lang="">
    <div>
        <h1>Page numéro {{ page.number }} du document {{document.title}} </h1>
        <h5> Voici le texte de la page : </h5>
        <p class="text-blue"> {{page.text}} </p>
    </div>
</template>
<script>
export default {
    props:{
        pageId : {
            type : Number,
            required : true
        }
    },
    data() {
        return {
            page: {},
            document: {}
        };
    },
    mounted(){
        this.getPage();
    },
    methods: {
        getPage() {
            fetch(`http://localhost:8000/api/v1/pages/${this.pageId}/`)
            .then(response => {
                if(!response.ok){
                    throw new Error("Error response");
                }
                return response.json();
            })
            .then(data => {
                this.page = data;
                this.getDocument();
            })
            .catch(error => {
                console.error('Erreur lors de la récupération des documents:', error);
            });
        },

        getDocument(){
            fetch(`http://localhost:8000/api/v1/documents/${this.page.document.id}/`)
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
}
</script>
<style lang="">
    
</style>
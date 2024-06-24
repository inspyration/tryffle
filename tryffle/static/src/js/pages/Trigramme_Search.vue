<template>
  <div class="container mt-5">
    <div class="input-group mb-3">
      <input 
        v-model="searchQuery" 
        @keyup.enter="searchTrigram" 
        placeholder="Rechercher par trigramme..." 
        class="form-control"
      />
      <div class="input-group-append">
        <button @click="searchTrigram" class="btn btn-primary">Rechercher</button>
      </div>
    </div>

    <ul v-if="pages.length > 0" class="list-group">
      <li v-for="page in pages" :key="page.id" class="list-group-item mb-3">
        <h3 class="text-secondary">Page {{ page.number }}</h3>
        <p>{{ page.text }}</p>
        <h4 class="text-info">Document: {{ page.document.title }}</h4>
        <p>{{ page.document.description }}</p>
      </li>
    </ul>

    <p v-else class="text-danger">Aucun résultat pour la recherche du mot : {{ searchQuery }}</p>
  </div>
</template>
  
  <script>
  export default {
    data() {
      return {
        searchQuery: '',
        pages: [],
        searchPerformed: false
      };
    },
    methods: {
      searchTrigram() {
        this.searchPerformed = true;
        fetch(`http://localhost:8000/api/v1/trigramme_search/?search=${this.searchQuery}`)
          .then(response => {
            if (!response.ok) {
              throw new Error('Erreur lors de la récupération des pages');
            }
            return response.json();
          })
          .then(data => {
            this.pages = data;
          })
          .catch(error => {
            console.error('Erreur lors de la recherche des pages:', error);
          });
      }
    }
  };
  </script>
  
  <style>
  /* Ajoutez des styles spécifiques à ce composant ici si nécessaire */
  </style>
  
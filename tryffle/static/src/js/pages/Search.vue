<template>
    <div>
      <input v-model="searchQuery" @keyup.enter="searchPages" placeholder="Rechercher un text..." />
      <button @click="searchPages">Rechercher</button>
      <ul v-if="pages.length > 0">
        <li v-for="page in pages" :key="page.id">
        <h3>Page {{ page.number }}</h3>
        <p>{{ page.text }}</p>
        <h4>Document: {{ page.document.title }}</h4>
        <p>{{ page.document.description }}</p>
      </li>
      </ul>
      <p v-else>Aucun résultat pour la recherche du mot : {{searchQuery }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchQuery: '',
        pages: [], 
      };
    },
    methods: {
      searchPages() {
        fetch(`http://localhost:8000/api/v1/pages/?search=${this.searchQuery}`)
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
  
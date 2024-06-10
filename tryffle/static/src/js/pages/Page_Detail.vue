<template lang="">
    <div>
        <h1>Page numéro {{ page.number }} du document {{ page.document.title }} </h1>
        <h5> Voici le texte de la page : </h5>
        <p> {{page.text}} </p>
    </div>
</template>
<script>
export default {
    props:{
        page : {
            type : Array,
            required : true
        }
    }
}
</script>
<style lang="">
    
</style>
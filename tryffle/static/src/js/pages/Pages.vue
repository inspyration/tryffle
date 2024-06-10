<template lang="">
    <div>
        
        
        <ul v-for="page in pages" :key="index">
            <li><a :href="`page/${doc.id}/`">{{page.number}} : Cliquer pour plus de détails </a><li>
        </ul>
    </div>
</template>
<script>
export default {
    props : {
        pages : {
            type : Array, 
            required : true
        }
    }
}
</script>
<style lang="">
    
</style>
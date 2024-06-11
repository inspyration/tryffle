<template lang="">
    <div>
        <h1>Test</h1>
        <ul>
          <li v-for="page in pages" :key="page.number">
            <a :href="`page/${page.number}/`">Page {{ page.number }}</a>
          </li>
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
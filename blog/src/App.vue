<template>
  <div id="app">
    <Article title="Title" content="This is a content"/>
    <Article title="Title2" content="This is a content2"/>
  </div>
</template>

<script>
import Article from './components/Article.vue'

export default {
  name: 'App',
  components: {
    Article
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

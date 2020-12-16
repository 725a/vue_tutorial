<template>
    <div class="article">
        <div class="title">
            {{title}}
        </div>
        <div class="content">
            {{content}}
        </div>
    </div>
</template>

<script>
export default {
  name: 'Article',
  props: {
    title: String,
    content: String,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.title {
  margin: 40px 0 0;
  color: red;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

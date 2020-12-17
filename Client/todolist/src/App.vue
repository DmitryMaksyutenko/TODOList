<template>
  <div id="app">
    <Main/>
    <Create/>
    <Load/>
  </div>
</template>

<script>
import Main from './components/MainPage.vue'
import Create from './components/Create'
import Load from './components/Load'

export default {
  name: 'App',
  components: {
    Main,
    Create,
    Load
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
  display: flex;
  justify-content: center;
  height: 100%;
  background-color: rgb(231, 231, 222);
}

html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}
</style>

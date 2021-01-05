<template>
  <div id="app">
    <Main/>
    <Create/>
    <Load/>
    <List/>
    <AddTask/>
    <EditTask/>
  </div>
</template>

<script>
import Main from './components/Main.vue'
import Create from './components/Create'
import Load from './components/Load'
import List from './components/List'
import AddTask from './components/AddTask.vue'
import EditTask from './components/EditTask.vue'

export default {
  name: 'App',
  components: {
    Main,
    Create,
    Load,
    List,
    AddTask,
    EditTask
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  display: flex;
  justify-content: center;
  height: 100%;
  background-color: rgb(246, 246, 246);
}

html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}
</style>

<template>
    <div id="mainPage"
      v-show="$store.state.mainVisible"
      class="mainPage">

      <b-button-group vertical
       class="group">

        <b-button pill id="createButton" class="button"
          v-on:click="showCreate">Create List</b-button>

        <b-button pill id="loadButton" class="button"
          v-on:click="showLoad">Load List</b-button>

      </b-button-group>

    </div>
</template>

<script>

export default {

  name: 'MainPage',

  methods: {
    showCreate () {
      this.$store.commit('updateCreateVisibleState', true)
      this.$store.commit('updateLoadVisibleState', false)
      this.$store.commit('updateMainVisibleState', false)
    },

    showLoad () {
      this.$store.commit('updateLoadVisibleState', true)
      this.$store.commit('updateCreateVisibleState', false)
      this.$store.commit('updateMainVisibleState', false)
      this.$store.dispatch('getLists')
    }
  }

}
</script>

<style scoped>
.mainPage {
  width: 100%;
  height: 100%;
}

.group {
  width: 15%;
  height: 15%;
  margin-top: 30%;
}

.button {
  background-color: rgb(73, 109, 114);
  margin-bottom: 20%;
  font-size: 150%;
}

@media screen and (max-width: 500px) {

 .button {
   margin-bottom: 30%;
   font-size: 120%;
 }

 .group {
   height: 40%;
   width: 50%;
   margin-top: 55%;
 }

}

@media screen and (min-width: 1300px) {

 .button {
   margin-bottom: 20%;
   font-size: 150%;
 }

 .group {
   height: 20%;
   width: 15%;
   margin-top: 20%;
 }

}
</style>

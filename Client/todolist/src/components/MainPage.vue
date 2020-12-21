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
    }
  }

}
</script>

<style>
.mainPage {
  width: 100%;
  height: 100%;
}

.group {
  width: 50%;
  height: 50%;
  margin-top: 20%;
}

.button {
  background-color: rgb(73, 109, 114);
  margin-bottom: 20%;
  font-size: 200%;
}

@media screen and (max-width: 500px) {
 .button {
   margin-bottom: 75%;
  font-size: 120%;
 }

 .group {
   height: 80%;
   margin-top:35%;
 }
}

@media screen and (min-width: 1300px) {
 .button {
   margin-bottom: 25%;
  font-size: 200%;
 }

 .group {
   height: 80%;
   margin-top:10%;
 }
}
</style>

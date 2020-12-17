<template>
    <div id="main"
      v-show="$store.state.mainVisible"
      class="main">
      <b-button-group vertical
       class="group">
        <b-button pill class="button"
          v-on:click="showCreate">Create List</b-button>
        <b-button pill class="button"
          v-on:click="showLoad">Load List</b-button>
      </b-button-group>
    </div>
</template>

<script>
export default {

  name: 'Main',

  data () {
    return {
    }
  },

  methods: {
    showCreate () {
      this.hideAfterClick()
      this.$store.commit('updateCreateVisibleState', true)
    },

    showLoad () {
      this.hideAfterClick()
      this.$store.commit('updateLoadVisibleState', true)
    },

    hideAfterClick () {
      this.$store.commit('updateMainVisibleState', false)
    }
  }

}
</script>

<style>
.main {
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

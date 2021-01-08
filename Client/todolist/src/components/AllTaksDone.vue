<template>
    <div
        id="AllDone"
        v-show="$store.state.allDoneAreaVisible"
        class="add-area
        position-absolute">

        <p class="all-done-text">
            Delete completed task list?
        </p>

        <b-input-group-append>

        <b-button
            id="OkButton"
            class="col-3
            add-area-button"
            pill
            squared
            v-on:click="okClicked">
            Ok
        </b-button>

        <b-button
            id="CancelButton"
            class="col-3
            add-area-button"
            pill
            squared
            v-on:click="cancelClicked">
            Cencel
        </b-button>

        </b-input-group-append>

    </div>
</template>

<script>
export default {

  name: 'AllDone',

  methods: {

    okClicked () {
      this.$store.dispatch('deleteList')
      this.$store.commit('updateAllDoneAreaVisible', false)
      this.$store.commit('updateListIsNotActive', false)
      this.$store.commit('updateListVisibleState', false)
      this.$store.commit('updateMainVisibleState', true)
    },

    cancelClicked () {
      this.$store.commit('updateAllDoneAreaVisible', false)
      this.$store.commit('updateListIsNotActive', false)
    }
  }
}
</script>

<style scoped>

    .add-area {
        width: 70%;
        height: 30%;
        top: 20%;
        border-radius: 30px;
        box-shadow: 0 0 30px 8px rgba(0, 0, 0, 1);
        z-index: 1100;
        background-color: rgb(231, 231, 222);
        pointer-events: all;
    }

    .all-done-text {
        font-size: 200%;
        margin-top:5%;
    }

    .add-area-button {
        margin: 10%;
        margin-left: 20%;
        width: 10%;
        height: 12%;
        font-size: 120%;
        background-color: rgb(73, 109, 114);
    }

    @media screen and (max-width: 500px) {

        .add-area {
            width: 100%;
            height: 40%;
            margin-left: 0%;
        }

        .all-done-text {
            font-size: 150%;
            margin-top: 10%;
        }

        .add-area-button {
            width: 10%;
        }

    }

    @media screen and (min-width: 1300px) {

        .add-area-button {
            margin: 5%;
            margin-left: 22%;
        }

    }

</style>

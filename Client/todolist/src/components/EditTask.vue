<template>
    <div
        id="EditTaks"
        v-show="$store.state.editAreaVisible"
        class="add-area
        position-absolute">

        <b-form-input
            class="add-area-input"
            v-model="$store.state.editedTaskText">
            {{ $store.state.editedTaskText }}
        </b-form-input>

        <b-input-group-append>

        <b-button
            id="SaveButton"
            class="col-3
            add-area-button"
            pill
            squared
            :disabled="$store.state.editedTaskText === ''"
            v-on:click="editAreaSaveButtonClick">
            Save
        </b-button>

        <b-button
            id="CancelButton"
            class="col-3
            add-area-button"
            pill
            squared
            v-on:click="editAreaCancelButtonClick">
            Cencel
        </b-button>

        </b-input-group-append>
    </div>
</template>

<script>
export default {

  name: 'EditTask',

  methods: {
    editAreaSaveButtonClick () {
      this.$store.commit('editedTaskText', this.$store.state.editedTaskText.trim())
      this.resetToDefault()
    },

    editAreaCancelButtonClick () {
      this.resetToDefault()
    },

    resetToDefault () {
      this.$store.commit('updateEditAreaVisible', false)
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

.add-area-input {
    margin-top: 5%;
    margin-left: 5%;
    outline: 1px solid lightblue;
    width: 90%;
    height: 20%;
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

  .add-area-button {
    width: 10%;
  }

  .add-area-input {
    margin-top: 7%;
    height: 30%;
  }

}

@media screen and (min-width: 1300px) {

  .add-area-button {
    margin: 5%;
    margin-left: 22%;
  }

}

</style>

<template>
    <div id="Create"
      v-show="$store.state.createVisible"
      class="add-area
      position-absolute">

        <p
          id="exist-message"
          class="exist-message"
          v-show="$store.state.listErrorVisible">
          {{ errorMessage }}
        </p>

        <b-form-input
          maxlength="50"
          placeholder="Task description."
          class="add-area-input"
         v-model="$store.state.newListTitle">
        </b-form-input>

        <b-input-group-append>

        <b-button
            id="AddButton"
            class="col-3
            add-area-button"
            pill
            squared
            :disabled="$store.state.newListTitle === ''"
            v-on:click="createButton">
            Create
        </b-button>

        <b-button
            id="CancelButton"
            class="col-3
            add-area-button"
            pill
            squared
            v-on:click="cancelButton">
            Cencel
        </b-button>

    </div>
</template>

<script>
export default {

  name: 'Create',

  data () {
    return {
      errorMessage: 'safs'
    }
  },

  methods: {

    async createButton () {
      await this.$store.dispatch('doesListExists')
        .then(response => {
          this.$store.commit('updateListTitleError', true)
          if (response.data.exists) {
            this.errorMessage = 'List already exist.'
          } else {
            if (this.isUpperCase(this.$store.state.newListTitle[0])) {
              this.createActions()
              this.$store.dispatch('insertList')
            } else {
              this.errorMessage = 'List name must start with capital letter.'
            }
          }
        })
    },

    isUpperCase (letter) {
      const regexp = /^[A-Z]/
      return regexp.test(letter)
    },

    createActions () {
      this.$store.commit('newListTitle')
      this.$store.commit('updateMainVisibleState', false)
      this.$store.commit('updateCreateVisibleState', false)
      this.$store.commit('updateListVisibleState', true)
    },

    cancelButton () {
      this.$store.commit('updateCreateVisibleState', false)
      this.$store.commit('updateMainVisibleState', true)
      this.$store.commit('updateListExists', false)
      this.$store.commit('updateNewListTitle', '')
      this.errorMessage = ''
    }
  }
}
</script>

<style>

.exist-message {
  margin-top: 1%;
  color: red;
}

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
    margin-top: 4%;
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

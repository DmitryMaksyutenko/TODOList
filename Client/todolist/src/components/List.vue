<template>
    <div id="List"
        class="list"
        v-show="$store.state.listVisible"
        v-bind:class="{'not-active': listIsNotActive}">

        <div id="AddArea"
          v-show="addAreaVisible"
          class="add-area
          position-absolute">

          <b-form-input
            placeholder="Task description."
            class="add-area-input"
            v-model="newTaskText">
          </b-form-input>

          <b-input-group-append>

            <b-button
              id="AddAreaAddButton"
              class="col-3
              add-area-button"
              pill
              squared
              v-on:click="addAreaAddButtonClick">
                Add
            </b-button>

            <b-button
              id="AddAreaCancelButton"
              class="col-3
              add-area-button"
              pill
              squared
              v-on:click="addAreaCancelButtonClick">
                Cencel
            </b-button>

          </b-input-group-append>

        </div>

        <div v-if="$store.state.list.length === 0">
            <b-list-group-item>There are no list with tasks.</b-list-group-item>
        </div>

        <div v-else
          id="ListGroup"
          class="list">

            <b-list-group-item
             id="ListTitle"
             class="border
             border-primary
             list-title">{{ $store.state.list[0].title }}
            </b-list-group-item>

            <b-list-group
              id="ListGroup"
              class="lst-group overflow-auto">

                <b-list-group-item
                  id="ListItem"
                  class="lst-item d-flex"
                  v-for="task in $store.state.list[1].tasks"
                  v-bind:key="task">

                    <div class="flex-grow-1 list-content">
                      {{ task.content }}
                    </div>

                  <button type="button" class="btn btn-outline-secondary
                    list-item-button">
                    <img src="../assets/pencil.svg" class="list-item-button-img"/>
                  </button>

                  <button type="button" class="btn btn-outline-secondary
                    list-item-button">
                    <img src="../assets/delete.svg" class="list-item-button-img"/>
                  </button>

                </b-list-group-item>

            </b-list-group>

            <b-button
              id="AddButton"
              class="list-button"
              v-on:click="listAddButtonClick"
              pill>Add
            </b-button>

            <b-button
              id="SaveButton"
              class="list-button"
              pill>Save
            </b-button>

            <b-button
              id="DeleteButton"
              class="list-button"
              pill>Delete list
            </b-button>

        </div>

    </div>
</template>

<script>
export default {

  name: 'List',

  data () {
    return {
      addAreaVisible: false,
      isNotActive: false,
      newTaskText: ''
    }
  },

  methods: {
    listAddButtonClick () {
      this.addAreaVisible = true
      this.listIsNotActive = true
    },

    addAreaCancelButtonClick () {
      this.resetAddArea()
    },

    addAreaAddButtonClick () {
      this.$store.commit('addToList', this.newTaskText)
      this.resetAddArea()
    },

    resetAddArea () {
      this.listIsNotActive = false
      this.addAreaVisible = false
      this.newTaskText = ''
    }
  }

}
</script>

<style scoped>

.list {
    width: 100%;
    height: 99%;
}

.not-active {
  pointer-events: none;
}

.add-area {
  width: 70%;
  height: 30%;
  margin-left: 16%;
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

.list-title {
  width: 60%;
  margin-top: 1%;
  margin-left: 21%;
  font-size: 110%;
  background-color: rgb(238, 238, 238);
  user-select: none;
}

.lst-group {
  width: 60%;
  max-height: 80%;
  margin-top: 1%;
  margin-left: 21%;
}

.lst-item {
  margin: 2%;
  outline: 1px solid lightblue;
  user-select: none;
}

.list-content {
  height: 100%;
  text-align: left;
}

.list-item-button {
  padding: 0.5%;
  margin: 0.5%;
}

.list-item-button-img {
  margin: 0%;
  width: 24px;
}

.list-button {
  background-color: rgb(73, 109, 114);
  margin: 0.5%;
  width: 12%;
  height: 5%;
  font-size: 150%;
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

  .list-title {
    margin: 2%;
    width: 96%;
    font-size: 100%;
  }

  .lst-group {
    width: 96%;
    max-height: 70%;
    margin-top: 1%;
    margin-left: 2%;
  }

  .list-button {
    margin: 3%;
    width: 27%;
    height: 7%;
    font-size: 80%;
  }

  .list-item-button {
    margin: 0.5%;
  }
}

@media screen and (min-width: 1300px) {

  .add-area-button {
    margin: 5%;
    margin-left: 22%;
  }

  .load-button {
    margin: 0.5%;
  }
}
</style>

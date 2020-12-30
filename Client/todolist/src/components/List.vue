<template>
    <div id="List"
        class="list"
        v-show="$store.state.listVisible"
        v-bind:class="{'not-active': $store.state.listIsNotActive}">

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
                    <img src="../assets/check-mark.svg" class="list-item-button-img"/>
                  </button>

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
    }
  },

  methods: {
    listAddButtonClick () {
      this.$store.commit('updateAddAreaVisibleState', true)
      this.$store.commit('updateListIsNotActive', true)
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
  min-width: 80%;
  overflow-wrap: break-word;
  vertical-align: baseline;
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

  .lst-item {
    margin: 1%;
    padding: 0.1%;
  }

  .list-content {
    padding: 0%;
    min-width: 65%;
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

  .load-button {
    margin: 0.5%;
  }
}
</style>

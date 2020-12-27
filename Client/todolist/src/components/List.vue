<template>
    <div id="List"
        class="list"
        v-show="$store.state.listVisible">
        <div v-if="$store.state.list.length === 0">
            <b-list-group-item>There are no list with tasks.</b-list-group-item>
        </div>
        <div v-else
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
  name: 'List'
}
</script>

<style scoped>
.list {
    width: 100%;
    height: 99%;
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
  padding: 1%;
  margin: 0.5%;
}

.list-item-button-img {
  width: 32px;
}

.list-button {
  background-color: rgb(73, 109, 114);
  margin: 1%;
  width: 15%;
  height: 7%;
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

  .list-button {
    margin: 3%;
    width: 27%;
    font-size: 80%;
  }

  .list-item-button {
    margin: 0.5%;
  }
  .list-item-button-img {
    width: 24px;
  }
}

@media screen and (min-width: 1300px) {

  .load-button {
    margin: 1%;
  }
}
</style>

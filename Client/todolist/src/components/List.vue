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
                  v-bind:key="task"
                  v-bind:class="{'task-done': task.condition,
                                'task-not-complete': !task.condition}"
                  draggable
                  @drop="onDrop($event)"
                  @dragover.prevent
                  @dragenter.prevent
                  @dragstart="startDrag($event, task)">

                    <div class="flex-grow-1 list-content">
                      {{ task.content }}
                    </div>

                  <button
                    id="DoneButton"
                    @dragstart.prevent
                    type="button"
                    v-bind:key="task"
                    v-show="!task.condition"
                    v-on:click="doneButtonClicked(task)"
                    class="btn btn-outline-secondary
                          list-item-button">
                    <img src="../assets/check-mark.svg" class="list-item-button-img"/>
                  </button>

                  <button
                    id="EditButton"
                    type="button"
                    v-bind:key="task"
                    v-on:click="editButtonClicked(task)"
                    @dragstart.prevent
                    class="btn btn-outline-secondary
                          list-item-button">
                    <img src="../assets/pencil.svg" class="list-item-button-img"/>
                  </button>

                  <button
                    id="DeleteTaskButton"
                    type="button"
                    @dragstart.prevent
                    v-bind:key="task"
                    v-on:click="removeTaskFromList(task.content)"
                    class="btn btn-outline-secondary
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
              :disabled="$store.state.isAllTasksDone"
              pill>Save
            </b-button>

            <b-button
              id="DeleteButton"
              class="list-button"
              v-on:click="deleteList"
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
      taskUnderContent: ''
    }
  },

  methods: {

    listAddButtonClick () {
      this.$store.commit('updateAddAreaVisibleState', true)
      this.$store.commit('updateListIsNotActive', true)
    },

    deleteList () {
      this.$store.dispatch('deleteList')
      this.$store.commit('updateAllDoneAreaVisible', false)
      this.$store.commit('updateListIsNotActive', false)
      this.$store.commit('updateListVisibleState', false)
      this.$store.commit('updateMainVisibleState', true)
    },

    startDrag (e, item) {
      e.dataTransfer.dropEffect = 'move'
      e.dataTransfer.effectAllowed = 'move'
      e.dataTransfer.setData('draggedContent', item.content)
    },

    onDrop (e) {
      const underElemContent = e.srcElement.innerText
      const draggedContent = e.dataTransfer.getData('draggedContent')
      if (underElemContent !== draggedContent) {
        const draggedTask = this.$store.state.list[1].tasks
          .find(elem => elem.content === draggedContent)
        this.replaceTask(underElemContent, draggedTask)
      }
    },

    removeTaskFromList (content) {
      this.$store.state.list[1].tasks = this.$store.state.list[1].tasks
        .filter(value => value.content !== content)
    },

    replaceTask (underElemContent, draggedTask) {
      const len = this.$store.state.list[1].tasks.length
      for (let i = 0; i < len; i++) {
        if (this.$store.state.list[1].tasks[i].content === underElemContent) {
          this.removeTaskFromList(draggedTask.content)
          this.$store.state.list[1].tasks.splice(i, 0, draggedTask)
          break
        }
      }
    },

    doneButtonClicked (task) {
      task.condition = !task.condition
      this.allDone()
    },

    allDone () {
      if (this.$store.getters.isAllTasksComplete) {
        this.$store.commit('updateIsAllTasksDone', true)
        this.$store.commit('updateAllDoneAreaVisible', true)
        this.$store.commit('updateListIsNotActive', true)
      }
    },

    editButtonClicked (task) {
      this.$store.commit('updateEditAreaVisible', true)
      this.$store.commit('updateListIsNotActive', true)
      this.$store.commit('updateEditedTaskText', task.content)
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

.task-done {
  outline: 1px solid rgb(0, 163, 0);
}

.task-not-complete {
  outline: 1px solid lightcoral;
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

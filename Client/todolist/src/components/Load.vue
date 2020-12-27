<template>
    <div id="Load"
        v-show="$store.state.loadVisible"
        class="load">
        <b-list-group
        id="listGroup"
        class="lst-group overflow-auto">
          <div v-if="$store.state.lists.length === 0">
            <b-list-group-item>There are no lists with tasks.</b-list-group-item>
          </div>
          <b-list-group-item v-else
            id="listItem"
            v-for="list in $store.state.lists"
            v-bind:key="list"
            v-on:click="itemClickActions($event)"
            class="lst-item">
            {{ list }}
            </b-list-group-item>
        </b-list-group>
        <div class="d-inline">
          <b-button
           id="loadButton"
           v-on:click="loadButtonActions"
           :disabled="buttonLoadDisabled"
           pill
           class="load-button">Load
          </b-button>
          <b-button
           id="cancelButton"
           v-on:click="cancelButtonActions"
           pill
           class="load-button">Cancel
          </b-button>
        </div>
    </div>
</template>

<script>
export default {

  name: 'Load',

  data () {
    return {
      buttonLoadDisabled: true,
      selectedList: undefined
    }
  },
  methods: {
    itemClickActions (event) {
      this.buttonLoadDisabled = false
      this.listItemHiglight(event.target)
    },

    listItemHiglight (domElement) {
      this.removeClickedClassFromList()
      domElement.classList.add('lst-item-clicked')
      this.setSelectedList(domElement)
    },

    removeClickedClassFromList () {
      try {
        this.selectedList.classList.remove('lst-item-clicked')
      } catch (error) {}
    },

    setSelectedList (domElement) {
      this.selectedList = domElement
    },

    cancelButtonActions () {
      this.removeClickedClassFromList()
      this.selectedList = undefined
      this.buttonLoadDisabled = true
      this.$store.commit('updateLoadVisibleState', false)
      this.$store.commit('updateMainVisibleState', true)
    },

    loadButtonActions () {
      this.removeClickedClassFromList()
      const title = this.selectedList.textContent
      this.selectedList = undefined
      this.buttonLoadDisabled = true
      this.$store.commit('updateLoadVisibleState', false)
      this.$store.commit('updateListVisibleState', true)
      this.$store.dispatch('getList', title)
    }
  }

}
</script>

<style>
.load {
  width: 100%;
  height: 100%;
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
.lst-item-clicked {
  outline: 3px solid rgb(122, 187, 209);
}

.load-button {
  background-color: rgb(73, 109, 114);
  margin: 3%;
  width: 20%;
  height: 10%;
  font-size: 200%;
}

@media screen and (max-width: 500px) {

  .lst-group {
    width: 96%;
    margin-top: 1%;
    margin-left: 2%;
  }

  .load-button {
    margin: 4%;
    width: 40%;
    font-size: 120%;
  }

}

@media screen and (min-width: 1300px) {

  .load-button {
    margin: 1%;
  }

}

</style>

import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import 'es6-promise'

Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    mainVisible: true,
    createVisible: false,
    loadVisible: false,
    listVisible: false,
    listIsNotActive: false,
    addAreaVisible: false,
    editAreaVisible: false,
    allDoneAreaVisible: false,
    isAllTasksDone: false,
    lists: [],
    list: [
      { title: '' },
      { tasks: [] }
    ],
    newTaskText: '',
    editedTaskText: '',
    oldTask: ''
  },

  getters: {

    isAllTasksComplete: (state) => {
      for (const task in state.list[1].tasks) {
        if (!state.list[1].tasks[task].condition) {
          return false
        }
      }
      return true
    }
  },

  mutations: {

    updateAllDoneAreaVisible (state, value) {
      this.state.allDoneAreaVisible = value
    },

    updateIsAllTasksDone (state, value) {
      this.state.isAllTasksDone = value
    },

    updateMainVisibleState (state, value) {
      this.state.mainVisible = value
    },

    updateCreateVisibleState (state, value) {
      this.state.createVisible = value
    },

    updateLoadVisibleState (state, value) {
      this.state.loadVisible = value
    },

    updateListIsNotActive (state, value) {
      this.state.listIsNotActive = value
    },

    updateListVisibleState (state, value) {
      this.state.listVisible = value
    },

    updateAddAreaVisibleState (state, value) {
      this.state.addAreaVisible = value
    },
    updateEditAreaVisible (state, value) {
      this.state.editAreaVisible = value
    },

    updateLists (state, value) {
      this.state.lists = value
    },

    updateList (state, value) {
      this.state.list = value
    },

    updateTaskText (state, value) {
      this.state.newTaskText = value
    },

    updateEditedTaskText (state, value) {
      this.state.editedTaskText = value
      this.state.oldTask = value
    },

    editedTaskText (state, newTask) {
      for (const task in this.state.list[1].tasks) {
        if (this.state.list[1].tasks[task].content === this.state.oldTask) {
          this.state.list[1].tasks[task].content = newTask
        }
      }
    },

    addToList (state, value) {
      const tmp = this.state.list[1].tasks
      this.state.list[1].tasks = [{
        content: value,
        condition: false
      }].concat(tmp)
      this.state.isAllTasksDone = false
    }
  },

  actions: {
    getLists (context) {
      var tmpLists = []
      axios.get('http://192.168.0.101:8001/lists/')
        .then(response => {
          for (const elem in response.data) {
            tmpLists.push(response.data[elem].title)
          }
        })
      context.commit('updateLists', tmpLists)
    },

    getList (context, title) {
      var tmpList = [
        { title: '' },
        { tasks: [] }
      ]
      axios.get('http://192.168.0.101:8001/list/' + title.trim())
        .then(response => {
          tmpList[0].title = response.data[0].title
          for (const elem in response.data[1].tasks) {
            tmpList[1].tasks.push(response.data[1].tasks[elem])
          }
          context.commit('updateList', tmpList)
        })
    },

    deleteList (context) {
      const data = JSON.stringify({ title: this.state.list[0].title.trim() })
      axios.post('http://192.168.0.101:8001/delete/',
        data,
        { headers: { 'Content-Type': 'application/json' } })
        .then(response => {})
    }
  }

})

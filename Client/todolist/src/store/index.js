import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import 'es6-promise'

Vue.use(Vuex)

const url = 'http://192.168.0.101:8001/'

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
    listErrorVisible: false,
    isAllTasksDone: false,
    lists: [],
    list: [
      { title: '' },
      { tasks: [] }
    ],
    newTaskText: '',
    newListTitle: '',
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

    updateNewListTitle (state, value) {
      this.state.newListTitle = value
    },

    updateEditedTaskText (state, value) {
      this.state.editedTaskText = value
      this.state.oldTask = value
    },

    updateListTitleError (state, value) {
      this.state.listErrorVisible = value
    },

    editedTaskText (state, newTask) {
      for (const task in this.state.list[1].tasks) {
        if (this.state.list[1].tasks[task].content === this.state.oldTask) {
          this.state.list[1].tasks[task].content = newTask
        }
      }
    },

    newListTitle (state) {
      this.state.list[0].title = this.state.newListTitle
      this.state.list[1].tasks = []
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
    async getLists (context) {
      var tmpLists = []
      await axios.get(url + 'lists/')
        .then(response => {
          for (const elem in response.data) {
            tmpLists.push(response.data[elem].title)
          }
        })
      context.commit('updateLists', tmpLists)
    },

    async getList (context, title) {
      var tmpList = [
        { title: '' },
        { tasks: [] }
      ]
      await axios.get(url + 'list/' + title.trim())
        .then(response => {
          tmpList[0].title = response.data[0].title
          for (const elem in response.data[1].tasks) {
            tmpList[1].tasks.push(response.data[1].tasks[elem])
          }
          context.commit('updateList', tmpList)
        })
    },

    async insertList (context) {
      const data = JSON.stringify([{ title: this.state.list[0].title.trim() }, { tasks: {} }])
      await axios.post(url + 'insert/',
        data,
        { headers: { 'Content-Type': 'application/json' } })
        .then(response => {})
    },

    async deleteList (context) {
      const data = JSON.stringify({ title: this.state.list[0].title.trim() })
      await axios.post(url + 'delete/',
        data,
        { headers: { 'Content-Type': 'application/json' } })
        .then(response => {})
    },

    async saveList (context) {
      const title = this.state.list[0]
      let data = [title, { tasks: {} }]
      for (var i = 0; i < this.state.list[1].tasks.length; i++) {
        data[1].tasks[i] = this.state.list[1].tasks[i]
      }
      data = JSON.stringify(data)
      await axios.post(url + 'update/',
        data,
        { headers: { 'Content-Type': 'application/json' } })
    },

    doesListExists (context) {
      return axios.get(url + 'exists/' +
                      this.state.newListTitle.trim())
    }
  }

})

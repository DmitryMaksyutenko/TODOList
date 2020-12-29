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
    lists: [],
    list: [
      { title: '' },
      { tasks: [] }
    ]
  },

  mutations: {
    updateMainVisibleState (state, value) {
      this.state.mainVisible = value
    },

    updateCreateVisibleState (state, value) {
      this.state.createVisible = value
    },

    updateLoadVisibleState (state, value) {
      this.state.loadVisible = value
    },

    updateListVisibleState (state, value) {
      this.state.listVisible = value
    },

    updateLists (state, value) {
      this.state.lists = value
    },

    updateList (state, value) {
      this.state.list = value
    },

    addToList (state, value) {
      const tmp = this.state.list[1].tasks
      this.state.list[1].tasks = [{
        content: value,
        condition: false
      }].concat(tmp)
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
    }
  }

})

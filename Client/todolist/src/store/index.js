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
    lists: []
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
    updateLists (state, value) {
      this.state.lists = value
    }
  },

  actions: {
    getLists (context) {
      var tmpLists = []
      axios.get('http://127.0.0.1:8001/lists/')
        .then(response => {
          for (const obj in response.data) {
            tmpLists.push(response.data[obj].title)
          }
        })
      context.commit('updateLists', tmpLists)
    }
  }

})

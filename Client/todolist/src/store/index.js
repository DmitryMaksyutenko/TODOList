import Vue from 'vue'
import Vuex from 'vuex'
import 'es6-promise'

Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    mainVisible: true,
    createVisible: false,
    loadVisible: false
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
    }
  }

})

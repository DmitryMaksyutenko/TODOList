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
      state.mainVisible = value
    },
    updateCreateVisibleState (state, value) {
      state.createVisible = value
    },
    updateLoadVisibleState (state, value) {
      state.loadVisible = value
    }
  }

})

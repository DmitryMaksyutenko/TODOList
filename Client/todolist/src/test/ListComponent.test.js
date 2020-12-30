import { shallowMount, createLocalVue } from '@vue/test-utils'

import Vuex from 'vuex'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import List from '../components/List.vue'
import store from '../store/index'

const localVue = createLocalVue()
localVue.use(Vuex)
localVue.use(BootstrapVue)
localVue.use(BootstrapVueIcons)

describe('List.vue', () => {
  let wrapper

  beforeEach(() => {
    wrapper = shallowMount(List, { store, localVue })
    store.commit('updateListVisibleState', true)
  })

  it('List Add button test.', async () => {
    await wrapper.find('#AddButton').trigger('click')
    expect(store.state.addAreaVisible).toBe(true)
    expect(store.state.listIsNotActive).toBe(true)
  })
})

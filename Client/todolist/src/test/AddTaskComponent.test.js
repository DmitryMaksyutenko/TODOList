import { shallowMount, createLocalVue } from '@vue/test-utils'

import Vuex from 'vuex'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import AddTask from '../components/AddTask.vue'
import store from '../store/index'

const localVue = createLocalVue()
localVue.use(Vuex)
localVue.use(BootstrapVue)
localVue.use(BootstrapVueIcons)

describe('AddTask.vue', () => {
  let wrapper

  beforeEach(() => {
    wrapper = shallowMount(AddTask, { store, localVue })
    store.commit('updateAddAreaVisibleState', true)
  })

  it('Add button test.', async () => {
    await wrapper.find('#AddButton').trigger('click')
    expect(store.state.list[1].tasks[0].content)
      .toBe(store.state.newTaskText)
    expect(store.state.addAreaVisible).toBe(false)
    expect(store.state.listIsNotActive).toBe(false)
    expect(store.state.newTaskText).toBe('')
  })

  it('Cancel button test.', async () => {
    await wrapper.find('#CancelButton').trigger('click')
    expect(store.state.addAreaVisible).toBe(false)
    expect(store.state.listIsNotActive).toBe(false)
    expect(store.state.newTaskText).toBe('')
  })
})

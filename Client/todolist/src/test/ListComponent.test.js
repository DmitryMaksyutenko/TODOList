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
    expect(wrapper.vm.addAreaVisible).toBe(true)
    expect(wrapper.find('#AddArea').isVisible()).toBe(true)
    expect(wrapper.vm.listIsNotActive).toBe(true)
  })

  it('Add area cancel button test.', async () => {
    await wrapper.find('#AddAreaCancelButton').trigger('click')
    expect(wrapper.vm.listIsNotActive).toBe(false)
    expect(wrapper.find('#AddArea').isVisible()).toBe(false)
    expect(wrapper.vm.newTaskText).toBe('')
  })

  it('Add area add button test.', async () => {
    await wrapper.find('#AddAreaAddButton').trigger('click')
    const task = store.state.list[1].tasks[0].content
    expect(task).toBe(wrapper.vm.newTaskText)
  })
})

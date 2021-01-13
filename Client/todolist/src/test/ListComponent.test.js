import { shallowMount, createLocalVue } from '@vue/test-utils'

import Vuex from 'vuex'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import List from '../components/List.vue'
import store from '../store/index'

store.state.list[1].tasks.push({ content: 'test', condition: false })

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

  it('Task complited button test.', async () => {
    expect(wrapper.find('#ListItem').classes('task-not-complete')).toBe(true)
    expect(wrapper.find('#DoneButton').isVisible()).toBe(true)
    await wrapper.find('#DoneButton').trigger('click')
    expect(wrapper.find('#ListItem').classes('task-done')).toBe(true)
    expect(wrapper.find('#DoneButton').isVisible()).toBe(false)
  })

  it('Task edit button pressed.', async () => {
    expect(store.state.editAreaVisible).toBe(false)
    await wrapper.find('#EditButton').trigger('click')
    expect(store.state.editAreaVisible).toBe(true)
    expect(store.state.listIsNotActive).toBe(true)
  })

  it('Task delete button test.', async () => {
    expect(store.state.list[1].tasks.length).toBe(1)
    await wrapper.find('#DeleteTaskButton').trigger('click')
    expect(store.state.list[1].tasks.length).toBe(0)
  })
})

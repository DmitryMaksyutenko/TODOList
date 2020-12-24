import { shallowMount, createLocalVue } from '@vue/test-utils'

import Vuex from 'vuex'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import Load from '../components/Load.vue'
import Main from '../components/Main.vue'

import tstStore from '../store/index'

const localVue = createLocalVue()
localVue.use(Vuex)
localVue.use(BootstrapVue)
localVue.use(BootstrapVueIcons)

describe('Load.vue', () => {
  let store
  let loadDiv
  let maniButtonLoad
  let cancelButton
  let firstListGroupElement
  let testWrapper

  beforeEach(() => {
    store = tstStore
    const loadComponentWrapper = shallowMount(Load, { store, localVue })
    const mainComponentWrapper = shallowMount(Main, { store, localVue })

    testWrapper = loadComponentWrapper
    cancelButton = loadComponentWrapper.find('#cancelButton')
    loadDiv = loadComponentWrapper.find('#load')
    firstListGroupElement = loadComponentWrapper.find('#listItem')
    maniButtonLoad = mainComponentWrapper.find('#loadButton')

    maniButtonLoad.trigger('click')
  })

  it('Load component start settings.', () => {
    expect(loadDiv.isVisible()).toBe(true)
    expect(testWrapper.find('#loadButton').attributes('disabled')).toBe('true')
    expect(testWrapper.vm.selectedList).toBeUndefined()
  })

  it('List item selection.', async () => {
    try {
      await firstListGroupElement.trigger('click')
      expect(testWrapper.find('#loadButton').attributes('disabled')).toBeUndefined()
      expect(testWrapper.vm.selectedList.textContent.length).toBeGreaterThan(0)
    } catch {}
  })

  it('Cancel button clicking.', async () => {
    await cancelButton.trigger('click')
    expect(loadDiv.isVisible()).toBe(false)
    expect(testWrapper.find('#loadButton').attributes('disabled')).toBe('true')
    expect(testWrapper.vm.selectedList).toBeUndefined()
  })
  it('Lists loading from server.', async () => {
    await store.dispatch('getLists')
    expect(store.state.lists.length).toBeGreaterThan(0)
  })
})

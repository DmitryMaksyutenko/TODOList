import { shallowMount, createLocalVue } from '@vue/test-utils'

import Vuex from 'vuex'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import tstStore from '../store/index'
import Main from '../components/Main.vue'
import Create from '../components/Create.vue'
import Load from '../components/Load.vue'

const localVue = createLocalVue()
localVue.use(Vuex)
localVue.use(BootstrapVue)
localVue.use(BootstrapVueIcons)

describe('Main.vue', () => {
  let store
  let mainDiv
  let createDiv
  let loadDiv
  let buttonLoad
  let buttonCreate

  beforeEach(() => {
    store = tstStore
    const mainComponentWrapper = shallowMount(Main, { store, localVue })
    const createComponentWrapper = shallowMount(Create, { store, localVue })
    const loadComponentWrapper = shallowMount(Load, { store, localVue })

    mainDiv = mainComponentWrapper.find('#mainPage')
    createDiv = createComponentWrapper.find('#create')
    loadDiv = loadComponentWrapper.find('#Load')
    buttonLoad = mainComponentWrapper.find('#loadButton')
    buttonCreate = mainComponentWrapper.find('#createButton')
  })

  it('Is mainComponent visible, other not.', () => {
    expect(mainDiv.isVisible()).toBe(true)
    expect(createDiv.isVisible()).toBe(false)
    expect(loadDiv.isVisible()).toBe(false)
  })
  it('Load button clicked.', async () => {
    await buttonLoad.trigger('click')
    expect(mainDiv.isVisible()).toBe(false)
    expect(createDiv.isVisible()).toBe(false)
    expect(loadDiv.isVisible()).toBe(true)
  })
  it('Create button clicked.', async () => {
    await buttonCreate.trigger('click')
    expect(mainDiv.isVisible()).toBe(false)
    expect(loadDiv.isVisible()).toBe(false)
    expect(createDiv.isVisible()).toBe(true)
  })
})

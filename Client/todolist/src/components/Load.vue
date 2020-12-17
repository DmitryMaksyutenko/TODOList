<template>
    <div id="load"
        v-show="$store.state.loadVisible"
        class="load">
        <b-list-group class="lst-group">
          <b-list-group-item
            v-for="list in Lists" v-bind:key="list"
            class="lst-item d-flex">
            <div class="flex-grow-1">{{ list }}</div>
            <b-button class="item-button">a</b-button>
            <b-button class="item-button">b</b-button>
            </b-list-group-item>
        </b-list-group>
    </div>
</template>

<script>
export default {

  name: 'Load',

  data () {
    return {
      Lists: [
        'some text 1',
        'some text 2',
        'some text 3',
        'some text 4'
      ]
    }
  }

}
</script>

<style>
.load {
  width: 100%;
  height: 100%;
}

.lst-group {
  width: 100%;
  margin-top: 1%;
}

.lst-item {
  margin: 1%;
  padding: 0.2%;
  font-size: 100%;
  border: 1px solid lightblue;
  text-align: left;
}

.item-button {
  margin: 0.5%;
}
</style>

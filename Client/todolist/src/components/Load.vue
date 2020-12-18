<template>
    <div id="load"
        v-show="$store.state.loadVisible"
        class="load">
        <b-list-group class="lst-group overflow-auto">
          <b-list-group-item
            v-for="list in Lists" v-bind:key="list"
            class="lst-item">
            {{ list }}
            </b-list-group-item>
        </b-list-group>
        <div class="d-inline">
          <b-button pill class="load-button">Load</b-button>
          <b-button pill class="load-button">Cencel</b-button>
        </div>
    </div>
</template>

<script>
export default {

  name: 'Load',

  data () {
    return {
      Lists: [
        'some text some text some text some text some text some text 1',
        'some text some text some text some text some text some text 2',
        'some text some text some text some text some text some text 3',
        'some text some text some text some text some text some text 4',
        'some text some text some text some text some text some text 5',
        'some text some text some text some text some text some text 6',
        'some text some text some text some text some text some text 7',
        'some text some text some text some text some text some text 8',
        'some text some text some text some text some text some text 9',
        'some text some text some text some text some text some text 11',
        'some text some text some text some text some text some text 12',
        'some text some text some text some text some text some text 13',
        'some text some text some text some text some text some text 14',
        'some text some text some text some text some text some text 15',
        'some text some text some text some text some text some text 16',
        'some text some text some text some text some text some text 17',
        'some text some text some text some text some text some text 18',
        'some text some text some text some text some text some text 19',
        'some text some text some text some text some text some text 20',
        'some text some text some text some text some text some text 21',
        'some text some text some text some text some text some text 22',
        'some text some text some text some text some text some text 23'
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
  width: 60%;
  max-height: 80%;
  margin-top: 1%;
  margin-left: 21%;
}

.lst-item {
  margin: 1%;
  font-size: 100%;
  border: 1px solid lightblue;
}

.load-button {
  background-color: rgb(73, 109, 114);
  margin: 3%;
  width: 20%;
  height: 10%;
  font-size: 200%;
}

@media screen and (max-width: 500px) {

.lst-group {
  width: 96%;
  max-height: 80%;
  margin-top: 1%;
  margin-left: 2%;
}

.load-button {
  margin: 4%;
  width: 40%;
  font-size: 120%;
}

}

@media screen and (min-width: 1300px) {

.load-button {
  margin: 1%;
}

}

</style>

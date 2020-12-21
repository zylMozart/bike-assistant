<template>
  <div class="home">
    <x-d-bike />
    <div class="d-flex pa-2" style="flex-wrap: wrap;justify-content: center;">
      <v-card
        min-width="80%"
        height="12rem"
        class="pa-2"
        rounded="xl"
        style="margin:1rem;padding:1rem;"
      >
        <v-card-title class="headline">
          Temperature <v-icon>mdi-thermometer</v-icon>
        </v-card-title>

        <v-card-text class="text-center" style="font-size:8rem">
          <br />
          <br />{{ temperature }}
        </v-card-text>
      </v-card>
      <v-card
        v-if="!frontLight"
        @click="switchFrontLight"
        min-width="35%"
        height="12rem"
        class="pa-2"
        color="red"
        rounded="xl"
        style="margin:1rem;padding:1rem;"
      >
        <v-card-title class="headline">
          Front Light <v-icon>mdi-light-switch</v-icon>
        </v-card-title>
        <v-card-text class="text-center" style="font-size:8rem">
          <br />
          <br />ON
        </v-card-text>
      </v-card>

      <v-card
        v-else
        @click="switchFrontLight"
        min-width="35%"
        height="12rem"
        class="pa-2"
        color="red"
        rounded="xl"
        style="margin:1rem;padding:1rem;"
      >
        <v-card-title class="headline">
          Front Light <v-icon>mdi-light-switch</v-icon>
        </v-card-title>
        <v-card-text class="text-center" style="font-size:8rem">
          <br />
          <br />OFF
        </v-card-text>
      </v-card>

      <v-card
        v-if="!backLight"
        @click="switchBackLight"
        min-width="40%"
        height="12rem"
        rounded="xl"
        class="pa-2"
        color="yellow"
        style="margin:1rem;padding:1rem"
      >
        <v-card-title class="headline">
          Back Light <v-icon>mdi-light-switch</v-icon>
        </v-card-title>
        <v-card-text class="text-center" style="font-size:8rem">
          <br />
          <br />ON
        </v-card-text>
      </v-card>

      <v-card
        v-else
        @click="switchBackLight"
        min-width="40%"
        height="12rem"
        class="pa-2"
        rounded="xl"
        color="yellow"
        style="margin:1rem;padding:1rem"
      >
        <v-card-title class="headline">
          Back Light <v-icon>mdi-light-switch</v-icon>
        </v-card-title>
        <v-card-text class="text-center" style="font-size:8rem">
          <br />
          <br />OFF
        </v-card-text>
      </v-card>
    </div>
  </div>
</template>

<script>
import XDBike from "@/components/3D-Bike.vue";

export default {
  name: "DashBoard",
  components: { XDBike },
  computed: {
    temperature() {
      return this.$store.state.environment.temperature;
    },
    frontLight: {
      get() {
        return this.$store.state.device.light.light1;
      },
      set(val) {
        this.$store.state.device.light.light1 = val;
      },
    },
    backLight: {
      get() {
        return this.$store.state.device.light.light2;
      },
      set(val) {
        this.$store.state.device.light.light2 = val;
      },
    },
  },
  methods: {
    switchFrontLight() {
      this.frontLight = !this.frontLight;
    },
    switchBackLight() {
      this.backLight = !this.backLight;
    },
  },
};
</script>

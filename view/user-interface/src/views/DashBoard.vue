<template>
  <div class="home">
    <x-d-bike />
    <div class="d-flex pa-2" style="flex-wrap: wrap;justify-content: center;">
      <v-card
        width="45%"
        height="10rem"
        class="pa-2"
        rounded="xl"
        style="margin:0.5rem;padding:0.2rem;"
      >
        <v-card-title class="headline">
          温度 <v-icon>mdi-thermometer</v-icon>
        </v-card-title>

        <v-card-text class="text-center content-text-m">
          {{ temperature }}
        </v-card-text>
      </v-card>
      <v-card
        width="45%"
        height="10rem"
        class="pa-2"
        rounded="xl"
        style="margin:0.5rem;padding:0.2rem;"
      >
        <v-card-title class="headline">
          气压 <v-icon>mdi-air-humidifier</v-icon>
        </v-card-title>

        <v-card-text class="text-center content-text-m">
          {{ pressure }}
        </v-card-text>
      </v-card>
      <v-card
        width="45%"
        height="10rem"
        class="pa-2"
        rounded="xl"
        style="margin:0.5rem;padding:0.2rem;"
      >
        <v-card-title class="headline">
          高度 <v-icon>mdi-altimeter</v-icon>
        </v-card-title>

        <v-card-text class="text-center content-text-m">
          {{ altitude }}
        </v-card-text>
      </v-card>
      <v-card
        width="45%"
        height="10rem"
        class="pa-2"
        rounded="xl"
        style="margin:0.5rem;padding:0.2rem;"
      >
        <v-card-title class="headline">
          速度 <v-icon>mdi-speedometer</v-icon>
        </v-card-title>

        <v-card-text class="text-center content-text-m">
          {{ speed }}
        </v-card-text>
      </v-card>
      <v-card
        width="80%"
        height="12rem"
        class="pa-2"
        rounded="xl"
        style="margin:1rem;padding:1rem;display:flex;align-items:center;
        background:url(https://www.bosch-ebike.com/fileadmin/_processed_/8/8/csm_Bosch-eBike-DTF-Elsass-MY2020-24_Print__300_dpi__p2_85567d1910.jpg?_=1592980405);"
        @click="$router.push('/cam')"
      >
        <v-card-text class="text-center content-text">
          Camera
        </v-card-text>
      </v-card>
      <v-card
        width="80%"
        height="12rem"
        class="pa-2"
        rounded="xl"
        style="margin:1rem;padding:1rem;display:flex;align-items:center;
        background:url(https://www.bosch-ebike.com/fileadmin/_processed_/8/8/csm_Bosch-eBike-DTF-Elsass-MY2020-24_Print__300_dpi__p2_85567d1910.jpg?_=1592980405);"
        @click="$router.push('/finder')"
      >
        <v-card-text class="text-center content-text">
          Bike Finder
        </v-card-text>
      </v-card>

      <v-card
        width="80%"
        height="12rem"
        class="pa-2"
        rounded="xl"
        style="margin:1rem;padding:1rem;display:flex;align-items:center;
        background:url(data:image/jpeg;base64,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);"
        @click="$router.push('/track')"
      >
        <v-card-text class="text-center content-text">
          Bike Tracker
        </v-card-text>
      </v-card>

      <v-card
        v-if="!frontLight"
        @click="switchFrontLight"
        width="40%"
        height="12rem"
        class="pa-2"
        color="red"
        rounded="xl"
        style="margin:0.5rem;padding:0.5rem;"
      >
        <v-card-title class="headline title-text">
          Front Light <v-icon>mdi-light-switch</v-icon>
        </v-card-title>
        <v-card-text class="text-center content-text-s">
          ON
        </v-card-text>
      </v-card>

      <v-card
        v-else
        @click="switchFrontLight"
        width="40%"
        height="12rem"
        class="pa-2"
        color="{frontLight:red}"
        rounded="xl"
        style="margin:0.5rem;padding:0.5rem;"
      >
        <v-card-title class="headline title-text">
          Front Light <v-icon>mdi-light-switch</v-icon>
        </v-card-title>
        <v-card-text class="text-center content-text-s">
          OFF
        </v-card-text>
      </v-card>

      <v-card
        v-if="!backLight"
        @click="switchBackLight"
        width="40%"
        height="12rem"
        rounded="xl"
        class="pa-2"
        color="yellow"
        style="margin:0.5rem;padding:0.5rem"
      >
        <v-card-title class="headline title-text">
          <v-icon>mdi-light-switch</v-icon>Back Light
        </v-card-title>
        <v-card-text class="text-center content-text-s">ON </v-card-text>
      </v-card>

      <v-card
        v-else
        @click="switchBackLight"
        width="40%"
        height="12rem"
        class="pa-2"
        rounded="xl"
        color="{backLight:yellow}"
        style="margin:0.5rem;padding:0.5rem"
      >
        <v-card-title class="headline title-text">
          Back Light <v-icon>mdi-light-switch</v-icon>
        </v-card-title>
        <v-card-text class="text-center content-text-s">
          OFF
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
    altitude() {
      return this.$store.state.environment.altitude;
    },
    speed() {
      return this.$store.state.environment.speed;
    },
    pressure() {
      return this.$store.state.environment.pressure;
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
<style scoped>
.content-text {
  font-size: 4rem;
  line-height: 1.2;
}
.content-text-s {
  font-size: 2rem;
  line-height: 1;
}
.content-text-m {
  font-size: 3rem;
  line-height: 1;
}
.title-text {
  word-break: break-word;
}
</style>

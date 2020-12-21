<template>
  <div class="home">
    <v-card class="mx-auto" max-width="344">
      <x-d-bike></x-d-bike>
    </v-card>
  </div>
</template>

<script>
// @ is an alias to /src
import XDBike from "@/components/3D-Bike.vue";

export default {
  name: "Posture",
  components: {
    XDBike,
  },
};
</script>

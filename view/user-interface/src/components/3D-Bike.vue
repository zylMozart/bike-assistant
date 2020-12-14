<template>
  <model-obj
  @on-load="onLoad"
    :backgroundAlpha="0"
    :controlsOptions="{
      enablePan,
      enableZoom,
      enableRotate,
    }"
    src="/models/obj/Sepeda Facific Invert.obj"
    mtl="/models/obj/Sepeda Facific Invert.mtl"
    :rotation="rotation"
  ></model-obj>
</template>
<script>
import { ModelObj } from "vue-3d-model";
export default {
  components: { ModelObj },
  data() {
    return {
      enablePan: true,
      enableZoom: false,
      enableRotate: false,
      rotation: {
        x: 0,
        y: 0,
        z: 0,
      },
    };
  },
  methods: {
    onLoad() {
      this.rotate();
    },
    rotate() {
      this.rotation.y += 0.01;
      requestAnimationFrame(this.rotate);
    },
  },
};
</script>

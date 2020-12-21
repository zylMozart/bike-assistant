<template>
  <div class="patrol_area">
    <div id="allmap" style="height:100vh;margin-top:5px;"></div>
    <v-btn @click="$router.push('../')" class="back-btn">Back</v-btn>
  </div>
</template>

<script>
export default {
  name: "BikeFinder",
  data() {
    return {
      map: "",
      geolocation: null,
      timer: null,
      mk: null,
      driving: null,
    };
  },
  mounted() {
    this.Start();
  },
  beforeDestroy() {
    clearInterval(this.timer);
  },
  methods: {
    Start() {
      this.map = new BMapGL.Map("allmap");
      let map = this.map;
      map.centerAndZoom(new BMapGL.Point(121.814224, 31.156484), 17);
      map.enableScrollWheelZoom(true);

      this.geolocation = new BMapGL.Geolocation();
      this.mk = new BMapGL.Marker(new BMapGL.Point(121.814224, 31.156484));

      this.map.addOverlay(this.mk);
      this.timer = setInterval(this.updatePos, 1000);
      this.driving = new BMapGL.WalkingRoute(this.map, {
        renderOptions: { map: this.map, autoViewport: false },
      });
    },
    updatePos() {
      let that = this;
      this.geolocation.getCurrentPosition(
        function(r) {
          if (this.getStatus() == BMAP_STATUS_SUCCESS) {
            that.map.panTo(r.point);
            that.mk.setPoint(r.point);
            var p1 = r.point;
            var p2 = new BMapGL.Point(120.1, 30.25);

            that.driving.search(p1, p2);
          } else {
            alert("failed" + this.getStatus());
          }
        },
        { enableHighAccuracy: true }
      );
    },
  },
};
</script>

<style lang="css" scoped>
.container {
  margin: 30px;
}
.text {
  font-size: 30px;
  line-height: 46px;
}
.back-btn {
  position: absolute;
  bottom: 0;
  z-index: 10;
}
#allmap {
  position: absolute;
  height: 100vh;
  width: 100vw;
}
</style>

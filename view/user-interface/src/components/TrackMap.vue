<template>
  <div class="patrol_area">
    <div id="allmap" style="height:600px;margin-top:5px;"></div>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
  data() {
    return {
      points: null,
      maps: "",
      pl: "",
      timer: null,
      mk: null,
    };
  },
  mounted() {
    this.pathStart();
  },
  methods: {
    async pathStart() {
      this.maps = new BMapGL.Map("allmap");
      this.maps.centerAndZoom(new BMapGL.Point(120.814224, 30.156484), 17);
      this.maps.enableScrollWheelZoom(true);

      let p = await this.$store.dispatch("updateGeo");
      this.pl = new BMapGL.Polyline([
        new BMapGL.Point(p.latitude, p.longitude),
        new BMapGL.Point(p.latitude, p.longitude),
      ]);
      this.maps.addOverlay(this.pl);

      let list = pl.getPath();
      list.push(new BMapGL.Point(130.814224, 30.156484));
      pl.setPath(list);

      this.mk = new BMapGL.Marker(new BMapGL.Point(130.814224, 30.156484));

      this.map.addOverlay(this.mk);
      this.timer = setInterval(this.updatePotion, 1000);
    },
    async updatePotion() {
      let p = await this.$store.dispatch("updateGeo");
      let list = this.pl.getPath();
      const point=new BMapGL.Point(p.latitude, p.longitude);
      list.push(point);
      this.pl.setPath(list);
      that.map.panTo(point);

    },
  },
  beforeDestroy() {
    clearInterval(this.timer);
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
</style>

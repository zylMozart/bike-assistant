<template>
  <div class="patrol_area">
    <div id="allmap" style="height:600px;margin-top:5px;"></div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Dashboard",
  data() {
    return {
      path: [
        {
          lng: 121.814224,
          lat: 31.156484,
        },
        {
          lng: 121.808547,
          lat: 31.165754,
        },
        {
          lng: 121.796186,
          lat: 31.184848,
        },
        {
          lng: 121.788353,
          lat: 31.192015,
        },
        {
          lng: 121.771752,
          lat: 31.194734,
        },
        {
          lng: 121.74969,
          lat: 31.189791,
        },
        {
          lng: 121.754217,
          lat: 31.179658,
        },
        {
          lng: 121.757523,
          lat: 31.167794,
        },
      ],
      maps: "",
      pls: "",
    };
  },
  mounted() {
    this.pathStart();
  },
  computed: {
    ...mapGetters(["name"]),
  },
  methods: {
    // 创建地图实例,并给设置移动路径
    pathStart() {
      // GL版命名空间为BMapGL
      // 按住鼠标右键，修改倾斜角和角度
      var map = new BMapGL.Map("allmap"); // 创建Map实例
      map.centerAndZoom(new BMapGL.Point(121.814224, 31.156484), 17); // 初始化地图,设置中心点坐标和地图级别
      map.enableScrollWheelZoom(true); //开启鼠标滚轮缩放

      var point = [];
      for (var i = 0; i < this.path.length; i++) {
        point.push(new BMapGL.Point(this.path[i].lng, this.path[i].lat));
      }
      var pl = new BMapGL.Polyline(point);

      this.maps = map;
      this.pls = pl;
      setTimeout(this.start, 3000);

      map.setHeading(64.5);
      map.setTilt(73);
    },
    // 创建个轨迹动画对象，并配置参数
    start() {
      var trackAni = new BMapGLLib.TrackAnimation(this.maps, this.pls, {
        overallView: true,
        tilt: 30,
        duration: 20000,
        delay: 300,
      });
      trackAni.start();
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
</style>

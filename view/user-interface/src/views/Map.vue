<template>
  <div class="container">
    
  </div>
</template>

<script>
export default {
  name: "Map",
  data() {
    return {
      h3tit: "人员轨迹",
      timer: null, //单人定时
      manyTime: null, //多人实时
      markerSpeed: 200,
      speedCount: 1,
      pName: "---",
      lineArr: [
        [116.478935, 39.997761],
        [116.478939, 39.997825],
        [116.478912, 39.998549],
        [116.478912, 39.998549],
        [116.478998, 39.998555],
        [116.478998, 39.998555],
        [116.479282, 39.99856],
        [116.479658, 39.998528],
      ],
      marker: {},
      map: {},
      markers: [], //点的集合  用来清除点标记
      firstArr: [120.11296645567579, 30.290059843858472],
      polyline: {},
      passedPolyline: {},
    };
  },
  methods: {
    initMap() {
      this.map = new AMap.Map("container", {
        resizeEnable: true,
        center: this.firstArr,
        zoom: 20,
      });

      this.marker = new AMap.Marker({
        map: this.map,
        position: this.firstArr,
        icon: pic,
        // offset: new AMap.Pixel(-25, 0),
        // autoRotation: true,
        // angle: 0
      });
      //覆盖物的圈圈
      this.circle = new AMap.Circle({
        center: this.firstArr,
        map: this.map,
        radius: 100,
        fillColor: "blue",
        strokeWeight: 1,
        strokeColor: "white",
        fillOpacity: 0.1,
      });
      this.circle1 = new AMap.Circle({
        center: this.firstArr,
        map: this.map,
        radius: 150,
        fillColor: "blue",
        strokeWeight: 1,
        strokeColor: "white",
        fillOpacity: 0.05,
      });
      // 绘制轨迹
      this.polyline = new AMap.Polyline({
        map: this.map,
        path: this.lineArr,
        showDir: true,
        strokeColor: "#28F", //线颜色
        // strokeOpacity: 1,     //线透明度
        strokeWeight: 6, //线宽
        // strokeStyle: "solid"  //线样式
      });
      // 设置鼠标划过点标记显示的文字提示
      // this.marker.setTitle("我是marker的title");

      // 设置label标签
      // label默认蓝框白底左上角显示，样式className为：amap-marker-label
      this.marker.setLabel({
        offset: new AMap.Pixel(50, 0), //设置文本标注偏移量
        content: `<div class='info'>${this.pName}</div>`, //设置文本标注内容
        direction: "top", //设置文本标注方位
      });
      var passedPolyline = new AMap.Polyline({
        map: this.map,
        strokeColor: "#AF5", //线颜色
        //path: this.lineArr,
        // strokeOpacity: 1,     //线透明度
        strokeWeight: 6, //线宽
        // strokeStyle: "solid"  //线样式
      });
      this.marker.on("moving", function(e) {
        passedPolyline.setPath(e.passedPath);
      });
      this.map.setFitView();
    },
    //实时轨迹
    currentAnimation(val) {
      this.flag = false;
      this.speedCount = 1;
      // this.marker.pauseMove();
      this.map.remove(this.marker);
      this.pName = val.person_name;
      if (this.timer) {
        clearInterval(this.timer);
        this.timer = null;
      }
      (后台的请求).then((data) => {
        if (data.statusCode == 200) {
          if (data.result.length > 0) {
            this.h3tit = "实时人员轨迹";
            this.lineArr = [];
            this.firstArr = [];
            data.result.forEach((item) => {
              this.lineArr.push([item.lng, item.lat]);
              this.firstArr.push(data.result[0].lng, data.result[0].lat);
            });
            this.initMap();
            this.startAnimation();
            if (this.firstArr.length > 0) {
              this.timer = setInterval(() => {
                后台的请求.then((data) => {
                  if (data.statusCode == 200) {
                    this.lineArr = [];
                    data.result.forEach((item) => {
                      this.lineArr.push([item.lng, item.lat]);
                    });
                    this.initroad();
                    this.startAnimation();
                  }
                });
              }, 2000);
            }
          } else {
            this.$message({
              message: "该人员没有安全帽实时数据",
              type: "warning",
            });
            this.firstArr = [120.11296645567579, 30.290059843858472];
            this.map = new AMap.Map("container", {
              resizeEnable: true,
              center: this.firstArr,
              zoom: 20,
            });
            this.marker = new AMap.Marker({
              map: this.map,
              position: this.firstArr,
              icon: pic,
            });
          }
        }
      });
    },
  },
};
</script>

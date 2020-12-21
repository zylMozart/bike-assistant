import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    device:{
      light:{
        light1:true,
        light2:true,
      }
    },
    environment:{
        geo:{
          lat:30,
          lng:122,
        },
        temperature:23.9
    }
    
  },
  mutations: {
    setTemperature(state, payload){
      state.environment.temperature=payload;
    },
    setLight1(state, payload){
      state.device.light.light1=payload;
    },
    setLight2(state, payload){
      state.device.light.light2=payload;
    },
    setGeo(state, payload){
      state.environment.geo=payload
    },
    getGeo(state, payload){
      return state.environment.geo
    }
  },
  actions: {
    async updateTemperature(context) {
      let res = await (await fetch("http://127.0.0.1:8001/temperature")).json();
      context.commit('setTemperature',res.data);
    },
    async getGeo(context) {
      let res = await (await fetch("http://127.0.0.1:8001/location")).json();
      context.commit('setGeo',res.data);
      return res.data;
    },
    async updateLight1(context,payload) {
      let res = await (await fetch("http://127.0.0.1:8001/set/light/"+payload)).json();
      context.commit('setLight1',res.data);
    },
    async updateLight2(context,payload) {
      let res = await (await fetch("http://127.0.0.1:8001/set/light"+payload)).json();
      context.commit('setLight2',res.data);
      
    },
  },
  modules: {
  }
})

import Vue from 'vue'
import VueRouter from 'vue-router'
import MapView from '../views/MapView.vue'
import DashBoard from '../views/DashBoard.vue'
import PostureView from '../views/PostureView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'DashBoard',
    component: DashBoard
  },
  {
    path: '/posture',
    name: 'Posture',
    component: PostureView
  },
  {
    path: '/map',
    name: 'Map',
    component: MapView
  }
]

const router = new VueRouter({
  routes
})

export default router

<template>
  <div class="home">
    <XDBike/>
  </div>
</template>

<script>
// @ is an alias to /src
import XDBike from '@/components/3D-Bike.vue'

export default {
  name: 'XDBike',
  components: {
    XDBike
  }
}
</script>

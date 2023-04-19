<template>
  <div>
    <Navbar />
    <section class="section">
    <router-view/>
    </section>
  </div>
</template>

<script>
import Navbar from '@/components/layout/NavBar'
import axios from 'axios'
export default { 
    name: 'App',
  	 components: {
      Navbar
    },
    // This is the beginning of the required information for the store
    beforeCreate() { 
      this.$store.commit('initializeStore')

      if (this.$store.state.token) { 
        axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
    } else { 
       axios.defaults.headers.common['Authorization'] = ""
       }
    }
  // And the end
  }
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>


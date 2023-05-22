<template>
  <div>
    <Navbar />
    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading' : $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>

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


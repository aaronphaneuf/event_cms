import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

require("./assets/main.scss")

axios.defaults.baseURL = 'http://127.0.0.1:8000'
// This is the address that Django runs on, not vue.

createApp(App).use(store).use(router, axios).mount('#app') //add axios to the use(router) function


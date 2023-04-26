import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import Events from '../views/dashboard/Events.vue'
import Event from '../views/dashboard/Event.vue'
import AddEvent from '../views/dashboard/AddEvent.vue'
import EditEvent from '../views/dashboard/EditEvent.vue'
import Test from '../views/dashboard/Test.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: { 
      requireLogin: true
    }
  },
  {
    path: '/dashboard/events',
    name: 'Events',
    component: Events,
    meta: { 
      requireLogin: true
    }
  },
  {
    path: '/dashboard/events/add',
    name: 'AddEvent',
    component: AddEvent,
    meta: { 
      requireLogin: true
    }
  },
  {
    path: '/dashboard/event/:id',
    name: 'Event',
    component: Event,
    meta: { 
      requireLogin: true
    }
},
{
  path: '/dashboard/editevent/:id',
  name: 'EditEvent',
  component: EditEvent,
  meta: { 
    requireLogin: true
  }
},
{
  path: '/dashboard/test/:id',
  name: 'Test',
  component: Test,
  meta: { 
    requireLogin: true
  }
},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => { 
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) { 
    next('/log-in')
  } else { 
    next()
  }
})

export default router

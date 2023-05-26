<template>
    <div class="container">
    <section class="hero">
  <div class="hero-body">
    <h1 class="title">Events</h1>
    <div class="field is-grouped">
  <div class="control">
    <div class="select">
  <select v-model="selectedYear">
    <option value="">All</option>
    <option v-for="year in uniqueYears" :key="year" :value="year">{{ year }}</option>
  </select>
</div>
  </div>
  <div class="control">
    <router-link to="/dashboard/events/add" class="button is-primary is-small">Add New Event</router-link>
  </div>


</div>
  </div>
</section>

<div class="columns is-multiline">
  <div class="column is-12">
    <div class="box">
      <div class="column is-12">
        <table class="table is-fullwidth is-striped is-hoverable">
          <thead>
            <tr>
              <th>Name</th>
              <th>Date</th>
              <th>Status</th>
              <th>Days Until Event</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(event, y) in filteredEvents" :key="event.id">
              <td>
                <router-link :to="{ name: 'Event', params: { id: event.id}}">{{ event.name }}</router-link>
              </td>
              <td>{{ event.date_time.event_date }}</td>
              <td><button class="button is-success is-light">On Sale</button></td>
              <td>{{ dates[y] }}</td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
    </div>
</template>
<script>
    import axios from 'axios'

    export default {
        name: 'Events',
        data() { 
            return { 
                events: [],
                today: '',
                dates: [],

                selectedYear: '',

                

            }
        },
        mounted() {
            this.getEvents()
        },

        computed: {
  filteredEvents() {
    if (this.selectedYear === '') {
      return this.events; // Return all events if no year is selected
    } else {
      // Filter events based on the selected year
      return this.events.filter(event => {
        return event.date_time.event_date.startsWith(this.selectedYear);
      });
    }
  },

  uniqueYears() {
    const yearsSet = new Set();
    this.events.forEach(event => {
      const year = new Date(event.date_time.event_date).getFullYear();
      yearsSet.add(year);
    });
    return Array.from(yearsSet);
  },
},

created() {
  this.getEvents();
},
        methods: {
            async getEvents() {
                this.$store.commit('setIsLoading', true)

                axios
                    .get('api/v1/simple_events/')
                    .then(response => { 
                        this.events = response.data

                        this.today = new Date()//.toISOString().split('T')[0];
                        
                        this.dates = this.events.map(({ date_time }) => Math.ceil((new Date(date_time.event_date) - this.today)/(1000 * 60 * 60 * 24)))

                        

                        for (let i = 0; i < this.dates.length; i++) {
                            if (this.dates[i] > 0) {
                                
                            } else {
                                this.dates[i] = 0;
                            }
                            }

                            this.$store.commit('setIsLoading', false);



                        

                    })
                    .catch(error => {
                        console.log(error)
                        this.$store.commit('setIsLoading', false);
                    })

                
                    
                
            }
        }
    }
</script>

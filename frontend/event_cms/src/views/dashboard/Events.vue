<template>
    <div class="container">
    <section class="hero">
            <div class="hero-body">
                <h1 class="title">Events</h1>
                <router-link to="/dashboard/events/add" class="button is-primary is-small">Add New Event</router-link>
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
                                <tr
                                    v-for="(event, y) in events"
                                    v-bind:key="event.id">
                                    <td>
                                        <router-link :to="{ name: 'Event', params: { id: event.id}}">{{event.name}}</router-link>
                                    </td>
                                    <td>{{ event.date_time.event_date }}</td>
                                    <td> <button class="button is-success is-light">On Sale</button></td>
                                    <td>{{dates[y]}}</td>
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

                

            }
        },
        mounted() {
            this.getEvents()
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

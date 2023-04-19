// Leads.vue

<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="columns is-multiline">
                <h1 class="title">Events</h1>

                <router-link to="/dashboard/events/add">Add New Event</router-link>
                
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Date</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="event in events"
                            v-bind:key="event.id">
                                <td><router-link :to="{ name: 'Event', params: { id: event.id}}">{{event.name}}</router-link></td>
                                <td>{{ event.date_time.event_date }}</td>
                        </tr>
                    </tbody>
                </table>
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
                events: []
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
                    })
                    .catch(error => { 
                        console.log(error)
                    })


                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>

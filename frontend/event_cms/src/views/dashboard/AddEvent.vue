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
                            <th>Company</th>
                            <th>Contact Person</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="lead in leads"
                            v-bind:key="lead.id">
                                <td>{{ lead.company }}</td>
                                <td>{{ lead.contact_person }}</td>
                                <td>{{ lead.status }}</td>
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
                    .get('api/v1/events/')
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

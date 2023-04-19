<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ event.name }}</h1>

                <router-link to="/" class="button is-light">Edit</router-link>

            </div>

                <div class="column is-6">
                    <div class="box">
                        <h2 class="subtitle">Details</h2>
                        <p><strong>Name: </strong> {{ event.name }} </p>
                        <p><strong>Description: </strong> {{ event.description }} </p>
                        <p><strong>Date: </strong> {{ date.event_date }} </p>
                        <p><strong>Entrance: </strong> {{ event.entrance }} </p>
                        <p><strong>Capacity: </strong> {{ event.capacity }} </p>
                        <p><strong>Held: </strong> {{ event.held }} </p>
                    </div>
                </div>

                <div class="column is-6">
                    <div class="box">
                        <h2 class="subtitle">Dates & Times</h2>
                        <p><strong>Doors Open: </strong> {{ date.door_open }} </p>
                        <p><strong>Doors Close: </strong> {{ date.door_close }} </p>
                        
                    </div>
                </div>

                <div class="column is-12">
                    <div class="box">
                        <h2 class="subtitle">Time Slots</h2>
                        <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Time Slot</th>
                            <th>Cap</th>
                            <th>Held</th>
                        </tr>
                        
                    </thead>
                    <tbody>
                        <tr
                            v-for="slot in time_slots">
                                <td>{{slot.time_range}}</td>
                                <td>{{slot.capacity }}</td>
                                <td>{{slot.held }}</td>
                        </tr>
                    </tbody>
                </table>
                        
                    </div>
                </div>

                <div class="column is-12">
                    <div class="box">
                        <h2 class="subtitle">Pricing</h2>
                        <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Price Type</th>
                            <th>Total Price</th>
                            <th>Layer 1</th>
                            <th>Layer 2</th>
                            <th>Layer 3</th>
                            <th>Layer 4</th>
                            <th>Layer 5</th>
                        </tr>
                        
                    </thead>
                    <tbody>
                        <tr
                            v-for="slot in time_slots">
                                <td>{{slot.time_range}}</td>
                                <td>{{slot.capacity }}</td>
                                <td>{{slot.held }}</td>
                        </tr>
                    </tbody>
                </table>
                        
                    </div>
                </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default { 
        name: 'Event',
        data() { 
            return { 
                event: {},
                date: '',
                time_slots: '',
            }
        },

        // This is to get the data from Django
        mounted() { 
            this.getEvent()
        },
        methods: { 
            async getEvent() { 
                this.$store.commit('setIsLoading', true)

                const EventID = this.$route.params.id

                axios
                    .get(`/api/v1/events/${EventID}/`)
                    .then(response => { 
                        this.event = response.data
                        this.date = this.event.date_time;
                        this.time_slots = this.event.timeslot_set;
                    })
                    .catch(error => { 
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>
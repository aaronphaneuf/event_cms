<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ event.name }}</h1>

                <router-link to="/" class="button is-light">Edit</router-link>

            </div>

                <div class="column is-12">
                    <div class="box">
                        <h2 class="subtitle">Description</h2>
                        <p> {{ event.description }} </p>
                    </div>
                </div>

                <div class="column is-6">
                    <div class="box">
                        <h2 class="subtitle">Details</h2>
                        <p><strong>Status </strong> {{ event.status }} </p>
                        <p><strong>Location: </strong> {{ location_name }} </p>
                        <p><strong>Facility: </strong> {{ facility_name }} </p>
                        <p><strong>Entrance: </strong> {{ event.entrance }} </p>
                        <p><strong>Capacity: </strong> {{ event.capacity }} </p>
                        <p><strong>Held: </strong> {{ event.held }} </p>
                        <p><strong>GR Required? </strong> {{ event.gr_required }} </p>
                        <p><strong>Early Closure? </strong> {{ event.early_closure }} </p>
                        
                    </div>
                </div>

                <div class="column is-6">
                    <div class="box">
                        <h2 class="subtitle">Dates & Times</h2>
                        <p><strong>Date(s): </strong> {{ date.event_date }} </p>
                        <p><strong>Event Start Time: </strong> {{ date.event_time }} </p>
                        <p><strong>Event End Time: </strong> {{ date.event_time }} </p>
                        <p><strong>Start Sell Date: </strong> {{ date.sell_date }} </p>
                        <p><strong>Stop Sell Date: </strong> {{ date.stop_date }} </p>
                        <p><strong>Doors Open: </strong> {{ date.door_open }} </p>
                        <p><strong>Doors Close: </strong> {{ date.door_close }} </p>
                        <p><strong>On Sale Date: </strong> {{ date.on_sale_date }} </p>
                        
                        
                        
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
                            <th>Layer 6</th>
                        </tr>

                        <tr>
                            <th>Example</th>
                            <th>Example</th>
                            
                            
                            <th v-for="layer in unique_price_layers">
                                {{ layer }}
                            </th>
                        </tr>



                        
                    </thead>
                    <tbody>
                        <tr
                            v-for="(x, y) in unique_price_types">
                            
                                
                                <td>{{ x.price_type }}</td>
                                <td>place_holder</td>
                                
                                
                                    <td v-for="price in unique_price_types">
                                    <td v-if="unique_price_layers[y]==x.price_layer[y]">Value
                                    </td>
                                    
                                </td>
                                <td>{{x.price_layer[y] }}</td>
                                
                                

                                
                               
                        </tr>
                        
                    </tbody>
                    

                    
                </table>


                <p v-for="(x,y) in unique_price_types"> GERE{{unique_price_layers[y]}}
                    <p v-for="a in x.price_layer"> {{a}}</p>
                    
                    
                    </p>
                        
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
                price_types_layers: '',
                location_name: '',
                facility_name: '',
                unique_price_types: '',
                unique_price_layers: '',
                
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
                        this.event = response.data;
                        this.location_name = this.event.location.location_name;
                        this.facility_name = this.event.facility.facility_name;
                        this.price_types_layers = this.event.price_layer_price;
                        this.date = this.event.date_time;
                        this.time_slots = this.event.timeslot_set;

                        this.unique_price_layers = [... new Set(this.event.price_layer_price.map(x=>x.price_layer))];

                        this.unique_price_types = Object.values(this.event.price_layer_price.reduce((value, object) => {

                            if (value[object.price_type]) {
                            ['price_layer'].forEach(key => value[object.price_type][key] = (value[object.price_type][key] + "," + object[key]).split(","));
                            ['price'].forEach(key => value[object.price_type][key] = (value[object.price_type][key] + "," + object[key] ).split(","));

                            
                            
                                    } else {
                                        value[object.price_type] = { ...object };
                                    }
                                    return value;
                                }, {}));


                       








                    })
                    .catch(error => { 
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>
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
                                <tr v-for="slot in time_slots">
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
                            <th>Price Layer</th>
                            <th v-for="price in unique_price_types">
                                {{ price }}
                            </th>
                        </tr>
                    </thead>
                        <tbody>
                            <tr v-for="layer in unique_price_layers">
                                <td>{{ layer }}</td>
                                <td v-for="(x, y) in unique_prices">
                                    <p v-for="(a, b) in unique_prices">
                                        <p v-if="x.price_layer[b] == layer">${{x.price[b]}}</p>
                                    </p>
                                </td>
                            </tr>
                            <tr>
                                <td><strong>Total</strong></td>
                                <td v-for="total in price_layer_sum"><strong>${{ total }}</strong></td>
                            </tr>
                        </tbody>
                        </table>
                    </div>
                </div>

                <div class="column is-12">
                    <div class="box">
                        <h2 class="subtitle">Discounts</h2>
                        <table class="table is-fullwidth">
                            <thead>
                                <tr>
                                    <th>Price Type</th>
                                    <th>Discount</th>
                                    <th>Description</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="discount in event.discount">
                                    <td>{{discount.price_type}}</td>
                                    <td>{{discount.discount }}</td>
                                    <td>{{discount.description }}</td>
                                </tr>
                            </tbody>
                        </table>  
                    </div>
                </div>

                <div class="column is-12">
                    <div class="box">
                        <h2 class="subtitle">GL Accounts</h2>
                        <table class="table is-fullwidth">
                            <thead>
                                <tr>
                                    <th>Price Layer</th>
                                    <th>GL Account</th>
                                    <th>Description</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="account in event.gl_account">
                                    <td>{{account.price_layer}}</td>
                                    <td>{{account.gl_account }}</td>
                                    <td>{{account.description }}</td>
                                </tr>
                            </tbody>
                        </table>  
                    </div>
                </div>


                <div class="column is-12">
                    <div class="box">
                        <h2 class="subtitle">CSI</h2>
                        <table class="table is-fullwidth">
                            <thead>
                                <tr>
                                    <th>CSI Needed?</th>
                                    <th>CSI Mandatory?</th>
                                    <th>Notes</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>{{event.csi_needed}}</td>
                                    <td>{{event.csi_mandatory}}</td>
                                    <td>{{event.csi_notes}}</td>
                                </tr>
                            </tbody>
                        </table>  
                    </div>
                </div>


                <div class="column is-12">
                    <div class="box">
                        <h2 class="subtitle">Web Links</h2>
                        <table class="table is-fullwidth">
                            <thead>
                                <tr>
                                    <th>Description</th>
                                    <th>Link</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Website:</td>
                                    <td>{{event.website_link}}</td>
                                </tr>
                                <tr>
                                    <td>Websales:</td>
                                    <td>{{event.websales_link}}</td>
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
                location_name: '',
                facility_name: '',
                unique_prices: '',
                unique_price_types: '',
                unique_price_layers: '',
                price_layer_sum: '',
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
                        this.date = this.event.date_time;
                        this.time_slots = this.event.timeslot_set;
                        
                        // Assign unique values to use as the pricing table column headers
                        this.unique_price_types = [... new Set(this.event.price_layer_price.map(x=>x.price_type))];

                        // Assign unique values to use as the pricing table column rows
                        this.unique_price_layers = [... new Set(this.event.price_layer_price.map(x=>x.price_layer))];

                        // Combine something like Object{price:56, price_layer: 'Ticket Price', price_type: 'Adult 18+'}
                        // And something like Object{price:40, price_layer: 'Food', price_type: 'Adult 18+'}
                        // Into Object{price_type: 'Adult 18+, price_layer: {0: "Ticket Price", 1: "Food"}, price: {0: 56, 1:40} }
                        this.unique_prices = Object.values(this.event.price_layer_price.reduce((value, object) => {
                            if (value[object.price_type]) {
                            ['price_layer'].forEach(key => value[object.price_type][key] = (value[object.price_type][key] + "," + object[key]).split(","));
                            ['price'].forEach(key => value[object.price_type][key] = (value[object.price_type][key] + "," + object[key] ).split(","));
                                    } else {
                                        value[object.price_type] = { ...object };
                                    }
                                    return value;
                                }, {}));

                        // Convert any left over into an array for both price and price_layer
                        this.unique_prices.forEach(el => 
                            (Array.isArray(el.price) ? el.price : [el.price]).forEach(
                                price => el.price = (Array.isArray(el.price) ? el.price : [el.price])))

                        this.unique_prices.forEach(el => 
                            (Array.isArray(el.price_layer) ? el.price_layer : [el.price_layer]).forEach(
                                price => el.price_layer = (Array.isArray(el.price_layer) ? el.price_layer : [el.price_layer])))

                        // Get the sum of each array in 'unique_prices'
                        const sum = (a, b) => Number(a) + Number(b);
                        this.price_layer_sum = this.unique_prices.map(({ price }) => price.reduce(sum));
                        
                    })
                    .catch(error => { 
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>
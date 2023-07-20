<template>
    <div class="container">
        <section class="hero">
        
            <div class="hero-body">
             <div class="hero-overlay"></div>
                <p class="title">
                    {{ event.name }}
                </p>
                <p class="subtitle">
                    {{ event.description }}
                    
                </p>
                 <router-link :to="editEventLink" class="button is-light">Edit</router-link>


            </div>
        </section>
        <div class="columns is-multiline">
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Details</h2>
                    <p><strong>Status </strong> {{ statusLabel }} </p>
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
                    <br>
                </div>
            </div>
            <div class="column is-12">
                <div class="box">
                    <h2 class="subtitle">Time Slots</h2>
                    <table class="table is-fullwidth is-striped">
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
                            <tr><td><strong>Total</strong></td><td><strong>{{ this.event.capacity }}</strong></td><td><strong>{{ this.event.held }}</strong></td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="column is-12">
                <div class="box">
                    <h2 class="subtitle">Pricing</h2>
                    <div class="table-container">
                        <table class="table is-fullwidth is-striped">
                            <thead>
                                <tr>
                                <tr></tr>
                                    <th v-for="(column, columnIndex) in columns" :key="columnIndex">{{column}}</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(record, rowIndex) in records" :key="rowIndex">
                                <td>{{record.name ? record.name : record.row}}</td>
                                    <td v-for="(detail, index) in record.details" :key="index">${{detail.value}}</td>
                                </tr>
                                <tr>
                                 <td><strong>Total</strong></td>
                                    <td v-for="(column, index) in columns" :key="index">
                                        <strong>${{ columnSums[column] }}</strong>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <div class="column is-12">
                <div class="box">
                    <h2 class="subtitle">Discounts</h2>
                    <table class="table is-fullwidth is-striped">
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
                    <table class="table is-fullwidth is-striped">
                        <thead>
                            <tr>
                                <th>Price Layer</th>
                                <th>GL Account</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="account in event.account">
                                <td>{{account.price_layer}}</td>
                                <td>{{account.gl_account.gl_account }}</td>
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
                    <h2 class="subtitle">Additional Notes</h2>
                    <p> {{ event.additional_notes }} </p>
                </div>
            </div>
            <div class="column is-12">
                <div class="box">
                    <h2 class="subtitle">Web Links</h2>
                    <table class="table is-fullwidth is-striped">
                        <thead>
                            <tr>
                                <th>Description</th>
                                <th>Link</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Website</td>
                                <td>{{event.website_link}}</td>
                            </tr>
                            <tr>
                                <td>Websales</td>
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
            prices_sum: '',


            columns: '', 
            rows: '',
            records: [],
            new_prices: [],
            new_price_layer_price: [],

           
        }
    },


     computed: {


        columnSums() {
            const sums = {};

            this.columns.forEach(column => {
                sums[column] = this.records.reduce((acc, record) => {
                    const detail = record.details.find(detail => detail.column === column);
                    return acc + Number(detail.value);
                }, 0);
            });

            return sums;
        },

        editEventLink() {
      const EventID = this.$route.params.id;
      return {
        name: 'EditEvent',
        params: { id: EventID }
      };
        },

       statusLabel() {
      // Map the Django status value to the corresponding label
      const statusMap = {
        OS: 'On Sale',
        P: 'Pending',
        S: 'Setup',
        AN: 'Action Needed',
        C: 'Concluded',
      };

      return this.event && this.event.status ? statusMap[this.event.status] : '';
    },

        
        
        
        
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
                    this.columns = [...new Set(this.event.price_layer_price.map(x => x.price_type))];

                    // Assign unique values to use as the pricing table column rows
                    this.rows = [...new Set(this.event.price_layer_price.map(x => x.price_layer))];    

                    this.rows.forEach(row => {
                        this.records.push({
                            row: row,
                            details: []
                        });
                    })

                    this.records.forEach(record => {
                        this.columns.forEach(column => {
                            record.details.push({
                                column: column,
                                value: 0
                            });
                        });
                    });

                   for (let i = 0; i < this.event.price_layer_price.length; i++) {
                        const myObject = this.event.price_layer_price[i];
                        const row = myObject.price_layer;
                        const column = myObject.price_type;
                        const value = myObject.price;

                        let record = this.new_prices.find(record => record.row === row);

                        if (!record) {
                            record = {
                            row,
                            details: []
                            };

                            this.new_prices.push(record);
                        }

                        record.details.push({
                            column,
                            value
                        });

                        // Check if there's a match in records and update the value
                        const recordToUpdate = this.records.find(record => record.row === row && record.details.some(detail => detail.column === column));
                        if (recordToUpdate) {
                            const detailToUpdate = recordToUpdate.details.find(detail => detail.column === column);
                            if (detailToUpdate) {
                            detailToUpdate.value = value;
                            }
                        }
                        }

                    // Assign unique values to use as the pricing table column headers
                    //this.unique_price_types = [...new Set(this.event.price_layer_price.map(x => x.price_type))];

                    // Assign unique values to use as the pricing table column rows
                    //this.unique_price_layers = [...new Set(this.event.price_layer_price.map(x => x.price_layer))];

                    // // Combine something like Object{price:56, price_layer: 'Ticket Price', price_type: 'Adult 18+'}
                    // // And something like Object{price:40, price_layer: 'Food', price_type: 'Adult 18+'}
                    // // Into Object{price_type: 'Adult 18+, price_layer: {0: "Ticket Price", 1: "Food"}, price: {0: 56, 1:40} }
                    // this.unique_prices = Object.values(this.event.price_layer_price.reduce((value, object) => {
                    //     if (value[object.price_type]) {
                    //         ['price_layer'].forEach(key => value[object.price_type][key] = (value[object.price_type][key] + "," + object[key]).split(","));
                    //         ['price'].forEach(key => value[object.price_type][key] = (value[object.price_type][key] + "," + object[key]).split(","));
                    //     } else {
                    //         value[object.price_type] = {
                    //             ...object
                    //         };
                    //     }
                    //     return value;
                    // }, {}));

                    // // Convert any left over into an array for both price and price_layer
                    // this.unique_prices.forEach(el =>
                    //     (Array.isArray(el.price) ? el.price : [el.price]).forEach(
                    //         price => el.price = (Array.isArray(el.price) ? el.price : [el.price])))

                    // this.unique_prices.forEach(el =>
                    //     (Array.isArray(el.price_layer) ? el.price_layer : [el.price_layer]).forEach(
                    //         price => el.price_layer = (Array.isArray(el.price_layer) ? el.price_layer : [el.price_layer])))

                    // // Get the sum of each array in 'unique_prices'
                    // const sum = (a, b) => Number(a) + Number(b);
                    // this.price_layer_sum = this.unique_prices.map(({
                    //     price
                    // }) => price.reduce(sum));

                    this.prices_sum = this.event.prices.map(a => Object.values(a).filter(v => typeof v === 'number').reduce((p, c) => p + c))

                    this.$store.commit('setIsLoading', false);
                    
                })
                .catch(error => {
                    console.log(error)
                    this.$store.commit('setIsLoading', false)
                })

            
        }
    }
}
</script>

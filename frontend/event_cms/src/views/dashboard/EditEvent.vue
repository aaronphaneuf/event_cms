<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="box">
                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <label>Name</label>
                            <div class="control">
                                <input type="text" class="input" v-model="event.name">
                            </div>
                        </div>
                        <div class="field">
                            <label>Description</label>
                            <div class="control">
                                <textarea class="textarea" v-model="event.description"></textarea>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <div class="columns is-multiline">
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Details</h2>
                    <div class="field">
                        <label>Location</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="location_name">
                                    <option>Unknown</option>
                                    <option v-for="location in all_locations">
                                        {{location.location_name}}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label>Facility</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="event.facility">
                                    >
                                    <option>Unknown</option>
                                    <option v-for="facility in all_facilities">
                                        {{facility.facility_name}}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label>Facility</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="event.entrance">
                                    >
                                    <option>North Entrance</option>
                                    <option>South Entrance</option>
                                    <option>West Entrance</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label>Capacity</label>
                        <input class="input" type="text" placeholder="Text input">
                    </div>
                    <div class="field">
                        <label>Held</label>
                        <input class="input" type="text" placeholder="Text input">
                    </div>
                    <div class="field">
                        <label>GR Required?</label>
                        <label class="radio">
                        <input type="radio" name="test">
                        Yes
                        </label>
                        <label class="radio">
                        <input type="radio" name="test">
                        No
                        </label>
                    </div>
                    <div class="field">
                        <label>Early Closure?</label>
                        <label class="radio">
                        <input type="radio" name="answer">
                        Yes
                        </label>
                        <label class="radio">
                        <input type="radio" name="answer">
                        No
                        </label>
                    </div>
                </div>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Dates & Times</h2>
                    <label>Event Date(s)</label>
                    <input type="date">
                    <label>Event Start Time: </label>
                    <input type="date" data-type="time">
                    <label>Event End Time: </label>
                    <input type="date" data-type="time">
                    <label>Start Sell Date:</label>
                    <input type="date" data-type="datetime">
                    <label>Stop Sell Date:</label>
                    <input type="date" data-type="datetime">
                    <label>Doors Open: </label>
                    <input type="date" data-type="time">
                    <label>Doors Close: </label>
                    <input type="date" data-type="time">
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
                                <td>
                                    <div class="select">
                                        <select v-model="slot.time_range">
                                            <option>{{slot.time_range}}</option>
                                            <option v-for="choice in time_slot_choices">{{choice}}</option>
                                        </select>
                                    </div>
                                </td>
                                <td><input type="text" class="input" v-model="slot.capacity"></td>
                                <td><input type="text" class="input" v-model="slot.held"></td>
                            </tr>
                            <div class="form-group">
                                <button @click="addTimeSlot" type="button" class="button is-primary is-small">Add Time Slot</button>
                            </div>
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
                                    <th></th>
                                    <th v-for="(column, columnIndex) in columns" :key="columnIndex">{{column}}</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(record, rowIndex) in records" :key="rowIndex">
                                    <td>{{record.name ? record.name : record.row}}</td>
                                    <td v-for="(detail, index) in record.details" :key="index">
                                        <input type="text" class="input" v-model="detail.value">
                                    </td>
                                </tr>
                                <tr>
                                    <td><strong>Total</strong></td>
                                    <td v-for="(column, index) in columns" :key="index">
                                        <strong>${{ columnSums[column] }}</strong>
                                    </td>
                                </tr>
                            </tbody>
                            <div class="select" style="display: inline-block; vertical-align: middle;" >
                                <select v-model="selectedName">
                                    <option v-for="name in names" :key="name" :value="name">{{ name }}</option>
                                </select>
                            </div>
                            <div style="display: inline-block;">
                                <button @click="addRow" class="button is-primary is-small">Add Row</button>
                            </div>
                            <div class="select" style="display: inline-block; vertical-align: middle;">
                                <select v-model="selectedColumn">
                                    <option v-for="name in names" :key="name" :value="name">{{ name }}</option>
                                </select>
                            </div>
                            <div style="display: inline-block;">
                                <button @click="addColumn" class="button is-primary is-small">Add Column</button>
                            </div>
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
    import bulmaCalendar from '../../../node_modules/bulma-calendar/dist/js/bulma-calendar.min.js'

    

    export default { 
        name: 'Event',
        data() { 
            return { 
                event: {},
                all_facilities: [],
                all_locations: [],
                bulma_date: new Date(),
                date: '',
                time_slots: '',
                time_slot_choices: ['6:00 - 6:30 AM', '6:30 - 7:00 AM'],
                location_name: '',
                
                
                
                unique_prices: '',
                unique_price_types: '',
                unique_price_layers: '',
                price_layer_sum: '',

                columns: '',//["A", "B", "C", "D"],
                rows: '',//["1", "2", "3", "4"],
                records: [],
                new_prices: [],

                names: ["John", "Jane", "Bob", "Alice"],
                selectedName: "",
                selectedColumn: "",
            }
        },

        
        mounted() { 
            this.getEvent();
           

           


            

        // Bulma calendar custom import

            const calendar = bulmaCalendar.attach(this.$refs.calendarTrigger, {
                startDate: this.bulma_date,
            })[0]
            calendar.on('select', e => (this.bulma_date = e.start || null))
            
        },

            computed: {
        niceDate() {
        if (this.bulma_date) {
            return this.bulma_date.toLocaleDateString()
        }
        },

        columnSums() {
      const sums = {};

      this.columns.forEach(column => {
        sums[column] = this.records.reduce((acc, record) => {
          const detail = record.details.find(detail => detail.column === column);
          return acc + Number(detail.value);
        }, 0);
      });

      return sums;
    }
    },
        methods: { 

            // Button to add a time slot
            addTimeSlot () {
                    this.time_slots.push({
                    })
                    },

            // Button to add a time slot

            submit () {
                const data = {
                    addTimeSlot: this.time_slots
                }
                alert(JSON.stringify(data, null, 2))
                },


            addRow() {
      const newRow = {
        row: this.selectedName,
        
        details: []
      };
      this.columns.forEach(column => {
        newRow.details.push({
          column: column,
          value: 0
        });
      });
      this.records.push(newRow);
    },


addColumn() {
      const newColumn = {
        
        column: this.selectedColumn,
      };
      this.columns.push(this.selectedColumn);
      this.records.forEach(record => {
        record.details.push({
          column: this.selectedColumn,
          value: 0
        });
      });
    },

       
  
            

         

            // This is to get the data from Django

            async getEvent() { 
                this.$store.commit('setIsLoading', true)

                const EventID = this.$route.params.id

                

                axios
                    .get(`/api/v1/editevent/${EventID}/`)
                    .then(response => { 
                        this.event = response.data;
                        this.location_name = this.event.location.location_name;
                        
                        this.date = this.event.date_time;
                        this.time_slots = this.event.timeslot_set;
                        
                        // Assign unique values to use as the pricing table column headers
                        this.columns = [... new Set(this.event.price_layer_price.map(x=>x.price_type))];

                        // Assign unique values to use as the pricing table column rows
                        this.rows = [... new Set(this.event.price_layer_price.map(x=>x.price_layer))];

                        //testing rows and columns


            
                        

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
                            }
                        
                    })
                    .catch(error => { 
                        console.log(error)
                    })

                axios
                .get('api/v1/facility/')
                .then(response => { 
                    this.all_facilities = response.data.reverse()
                })
                .catch(error => { 
                    console.log(error)
                })

                axios
                .get('api/v1/location/')
                .then(response => { 
                    this.all_locations = response.data.reverse()
                })
                .catch(error => { 
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
            },
            },

            
    }
</script>
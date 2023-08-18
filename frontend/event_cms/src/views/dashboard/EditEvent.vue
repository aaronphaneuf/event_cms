<template>
  <div class="container">
    <section class="hero">
      <div class="hero-body">
        <div class="hero-overlay"></div>
        <p class="title">Edit Event</p>
        <form @submit.prevent="submitForm">
          <div class="field">
            <div class="control">
              <button class="button is-light">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <div class="box">
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
                <select v-model="event.location">
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
                  <option v-for="facility in all_facilities">
                    {{facility.facility_name}}
                  </option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <label>Entrance</label>
            <div class="control">
              <div class="select">
                <select v-model="event.entrance">
                  <option>North Entrance</option>
                  <option>South Entrance</option>
                  <option>West Entrance</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <label>Capacity</label>
            <input class="input" type="number" v-model="event.capacity">
          </div>
          <div class="field">
            <label>Held</label>
            <input class="input" type="number" v-model="event.held">
          </div>
          <div class="field">
            <label>GR Required</label>
            <div class="control">
              <div class="select">
                <select v-model="event.gr_required">
                  <option>Yes</option>
                  <option>No</option>
                </select>
              </div>
            </div>
            <label>Early Closure</label>
            <div class="control">
              <div class="select">
                <select v-model="event.early_closure">
                  <option>Yes</option>
                  <option>No</option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Dates & Times</h2>
          <label>Event Date(s)</label>
          <input type="date" v-model="event_date">
            <label>Event Start Time:</label>
          <input type="text" data-type="time" v-model="event_time" ref="calendarTrigger2" >
            <label>Event End Time: </label>
          <input type="text" data-type="time" v-model="event_end_time" ref="calendarTrigger3">
            <label>Start Sell Date: </label>
          <input type="text" data-type="datetime" v-model="sell_date" ref="calendarTrigger4">
            <label>Stop Sell Date:</label>
          <input type="text" data-type="datetime" v-model="stop_date" ref="calendarTrigger5">
            <label>Doors Open: </label>
          <input type="text" data-type="time" v-model="door_open" ref="calendarTrigger6">
            <label>Doors Close: </label>
          <input type="text" data-type="time"  v-model="door_close" ref="calendarTrigger7">
            <label>Early Closure Time: </label>
          <input type="text" data-type="time"  v-model="early_closure_time" ref="calendarTrigger8">
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
            <tr v-for="(slot, index) in time_slots" :key="index">
              <td>
                <div class="select">
                  <select v-model="slot.time_range">
                    <option>{{ slot.time_range }}</option>
                    <option v-for="choice in time_slot_choices">{{ choice }}</option>
                  </select>
                </div>
              </td>
              <td><input type="number" class="input" v-model="slot.capacity"></td>
              <td><input type="number" class="input" v-model="slot.held"></td>
              <td><button class="delete" @click="removeTimeSlot(index)"></button></td>
            </tr>
            <tr>
              <td><strong>Total</strong></td>
              <td><strong>{{ capacity_held_total.capacity }}</strong></td>
              <td><strong>{{ capacity_held_total.held }}</strong></td>
            </tr>
            <div v-if="showError" class="notification is-danger">
              Capacity and held values do not match above in the 'Details' section.
            </div>
          </tbody>
        </table>
        <div class="form-group">
          <button @click="addTimeSlot" type="button" class="button is-primary is-small">Add Time Slot</button>
        </div>
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
                <th v-for="(column, columnIndex) in columns" :key="columnIndex">
                  {{ column }}
                  <button class="delete is-small" @click="removeColumn(columnIndex)"></button>
                </th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(record, rowIndex) in records" :key="rowIndex">
                <td>
                  {{ record.name ? record.name : record.row }}
                </td>
                <td v-for="(detail, index) in record.details" :key="index">
                 <input type="number" class="input" v-model="detail.value">
                </td>
                <td>
                  <button class="delete is-small" @click="removeRow(rowIndex)"></button>
                </td>
              </tr>
              <tr>
                <td><strong>Total</strong></td>
                <td v-for="(column, index) in columns" :key="index">
                  <strong>${{ columnSums[column] }}</strong>
                </td>
                <td></td>
              </tr>
            </tbody>
            <div class="select" style="display: inline-block; vertical-align: middle;">
              <select v-model="selectedName">
                <option v-for="name in all_pricelayers" :key="name" :value="name">{{ name }}</option>
              </select>
            </div>
            <div style="display: inline-block;">
              <button @click="addRow" class="button is-primary is-small">Add Price Layer</button>
            </div>
            <div class="select" style="display: inline-block; vertical-align: middle;">
              <select v-model="selectedColumn">
                <option v-for="name in all_pricetypes" :key="name" :value="name">{{ name }}</option>
              </select>
            </div>
            <div style="display: inline-block;">
              <button @click="addColumn" class="button is-primary is-small">Add Price Type</button>
            </div>
          </table>
        </div>
      </div>
    </div>
    <div class="column is-12">
      <div class="box">
        <h2 class="subtitle">Discounts</h2>
        <div class="table-container">
          <table class="table is-fullwidth is-striped">
            <thead>
              <tr>
               <th>Price Type</th>
               <th>Discount</th>
               <th>Description</th>
               <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(slot, index) in event.discount">
                <td>
                  <div class="select">
                    <select v-model="slot.price_type">
                      <option>{{ slot.price_type }}</option>
                      <option v-for="choice in all_pricetypes">{{ choice }}</option>
                    </select>
                  </div>
                </td>
                <td><input type="text" class="input" v-model="slot.discount"></td>
                <td><input type="text" class="input" v-model="slot.description"></td>
                <td>
                  <button @click="removeDiscount(index)" class="delete is-small"></button>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="form-group">
            <button @click="addDiscount" type="button" class="button is-primary is-small">Add Discount</button>
          </div>
        </div>
      </div>
    </div>
    <div class="column is-12">
      <div class="box">
        <h2 class="subtitle">GL Accounts</h2>
      <div class="table-container">
        <table class="table is-fullwidth is-striped">
          <thead>
            <tr>
              <th>Price Layer</th>
              <th>GL Account</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(acc, index) in account">
              <td>
                <div class="select">
                  <select v-model="acc.price_layer">
                    <option>{{ acc.price_layer }}</option>
                    <option v-for="choice in all_pricelayers">{{ choice }}</option>
                  </select>
                </div>
              </td>
              <td>
                <div class="select">
                  <select v-model="acc.account_data.gl_account">
                    <option v-if="acc.account_data.gl_account">{{ acc.account_data.gl_account }}</option>
                    <option v-for="choice in all_accounts">{{ choice.gl_account }}</option>
                  </select>
                </div>
              </td>
              <td>
                <button @click="removeAccount(index)" class="delete is-small"></button>
              </td>
            </tr>
          </tbody>
        </table> 
        <div class="form-group">
          <button @click="addAccount" type="button" class="button is-primary is-small">Add Account</button>
        </div>
      </div>
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
            <td>
              <div class="select">
                <select v-model="event.csi_needed">
                  <option>Yes</option>
                  <option>No</option>
                </select>
              </div>
            </td>
            <td>
              <div class="select">
                <select v-model="event.csi_mandatory">
                  <option>Yes</option>
                  <option>No</option>
                </select>
              </div>
            </td>
            <td>
              <div class="control">
                <input type="text" class="input" v-model="event.csi_notes">
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
    <div class="column is-12">
      <div class="box">
        <h2 class="subtitle">Additional Notes</h2>
        <div class="control">
          <textarea class="textarea" v-model="event.additional_notes"></textarea>
        </div>
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
              <td>
                <input type="text" class="input" v-model="event.website_link">
              </td>
            </tr>
            <tr>
              <td>Websales:</td>
              <td>
                <input type="text" class="input" v-model="event.websales_link">
              </td>
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
            showError: false,
            all_facilities: [],
            all_locations: [],
            all_pricetypes: [],
            all_pricelayers: [],
            date: '',
            time_slots: '',
            time_slot_choices: [    '6:00 - 6:30 AM',    '6:30 - 7:00 AM',    '7:00 - 7:30 AM',    '7:30 - 8:00 AM',    '8:00 - 8:30 AM',    '8:30 - 9:00 AM',    '9:00 - 9:30 AM',    '9:30 - 10:00 AM',    '10:00 - 10:30 AM',    '10:30 - 11:00 AM',    '11:00 - 11:30 AM',    '11:30 - 12:00 PM',    '12:00 - 12:30 PM',    '12:30 - 1:00 PM',    '1:00 - 1:30 PM',    '1:30 - 2:00 PM',    '2:00 - 2:30 PM',    '2:30 - 3:00 PM',    '3:00 - 3:30 PM',    '3:30 - 4:00 PM',    '4:00 - 4:30 PM',    '4:30 - 5:00 PM',    '5:00 - 5:30 PM',    '5:30 - 6:00 PM',    '6:00 - 6:30 PM',    '6:30 - 7:00 PM',    '7:00 - 7:30 PM',    '7:30 - 8:00 PM',    '8:00 - 8:30 PM',    '8:30 - 9:00 PM',    '9:00 - 9:30 PM',    '9:30 - 10:00 PM',    '10:00 - 10:30 PM',    '10:30 - 11:00 PM',    '11:00 - 11:30 PM',    '11:30 - 12:00 AM',    '12:00 - 12:30 AM'],
            capacity_held_total: { capacity: 0, held: 0 },
            selectedDate: null,
            selectedTime: null,
            discounts: null, 
            event_date: null,
            event_time: null,
            event_end_time: null,
            door_open: null,
            door_close: null,
            sell_date: null,
            sell_time: null,
            stop_date: null,
            stop_time: null,
            early_closure_time: null,
            account: null,
            all_accounts: null,
            unique_prices: '',
            unique_price_types: '',
            unique_price_layers: '',
            price_layer_sum: '',
            columns: '', //["A", "B", "C", "D"],
            rows: '', //["1", "2", "3", "4"],
            records: [],
            new_prices: [],
            new_price_layer_price: [],
            selectedName: "",
            selectedColumn: "",
        }
    },

    mounted() {
        this.getEvent();
    },

    watch: {
        start_date(newVal) {
            if (this.calendar1) {
                this.calendar1.setStartDate(newVal);
            }
            if (this.calendar4) {
                this.calendar4.setStartDate(newVal);
            }
            if (this.calendar5) {
                this.calendar5.setStartDate(newVal);
            }
        },
        start_time(newVal) {
            if (this.calendar2) {
                this.calendar2.setStartTime(newVal);
            }
            if (this.calendar3) {
                this.calendar3.setStartDate(newVal);
            }
            if (this.calendar6) {
                this.calendar6.setStartTime(newVal);
            }
            if (this.calendar7) {
                this.calendar7.setStartTime(newVal);
            }
            if (this.calendar8) {
                this.calendar8.setStartTime(newVal);
            }
        },
        time_slots: {
            handler: function(newVal) {
                let totalCapacity = 0
                let totalHeld = 0
                newVal.forEach(slot => {
                    totalCapacity += slot.capacity
                    totalHeld += slot.held
                })
                this.capacity_held_total = { capacity: totalCapacity, held: totalHeld 
            }
        },
        deep: true
    },

    records: {
        handler(newRecords) {
            const priceLayerPrice = [];
            // loop through each row in the records array
            newRecords.forEach((record) => {
                // loop through each detail in the row
                record.details.forEach((detail) => {
                    // only push an entry if the price is greater than 0
                    if (detail.value > 0) {
                        // create a new price object and add it to the priceLayerPrice array
                        priceLayerPrice.push({
                            price: detail.value,
                            price_layer: {
                                name: record.row
                            },
                            price_type: {
                            name: detail.column
                            }
                        });
                    }
                });
            });
            // update the price_layer_price data property with the new array
            this.new_price_layer_price = priceLayerPrice;
        },
        deep: true,
    },
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



},

methods: {
    // Button to add a discount
    addDiscount() {
        this.event.discount.push({})
    },
    // Button to remove discount
    removeDiscount(index) {
        this.event.discount.splice(index, 1);
    },
    // Button to add an Account
    addAccount() {
        this.account.push({
           // id: null,
            account_data: { gl_account: ''},
          price_layer: ''  
        });
    },

removeAccount(index) {
  this.account.splice(index, 1);
},



        // Button to add a time slot
        addTimeSlot() {
            this.time_slots.push({})
        },

        removeTimeSlot(index) {
      this.time_slots.splice(index, 1);
    },

        // Button to add a time slot

        submit() {
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

        removeRow(rowIndex) {
      this.records.splice(rowIndex, 1);
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

        removeColumn(columnIndex) {
      const removedColumn = this.columns.splice(columnIndex, 1);
      this.records.forEach((record) => {
        record.details.splice(columnIndex, 1);
      });
    },

//         updateAccountFields(index) {
//   const selectedFullName = this.account[index].account.full_name;

//   if (selectedFullName) {
//     const [glAccount, description] = selectedFullName.split(" - ");

//     const updatedAccount = {
//       ...this.account[index].account,
//       description: description,
//       gl_account: glAccount
//     };

//     this.$set(this.account, index, { ...this.account[index], account: updatedAccount });
//   }
// },

        // This is to get the data from Django

        async getEvent() {
            this.$store.commit('setIsLoading', true)

            const EventID = this.$route.params.id


            axios
                .get(`/api/v1/editevent/${EventID}/`)
                .then(response => {
                    this.event = response.data;


                    this.date = this.event.date_time;


                    this.event_date = this.event.date_time.event_date;
                    this.time_slots = this.event.timeslot_set;

                    this.event_date = this.date.event_date

                    this.account = this.event.account;

                    

                    //this.discounts = this.event.discount
                    


                    //const [event_start_hour, event_start_minute] = this.date.event_time.split(':');
                    this.event_time = this.date.event_time;

                    //const [event_end_hour, event_end_minute] = this.date.event_end_time.split(':');
                    this.event_end_time = this.date.event_end_time;

                    // const start_sell_date = this.date.sell_date;
                    // const start_sell_time = start_sell_date.split("T")[1].slice(0, -1);
                    // const [sell_hour, sell_minute] = start_sell_time.split(":");
                    // this.sell_time = `${sell_hour}:${sell_minute}`;
                    const sell_date_temp = new Date(this.date.sell_date);
                    this.sell_date = sell_date_temp.toLocaleDateString();
                    this.sell_time = sell_date_temp.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit', hour12: false});

                    // const end_sell_date = this.date.stop_date;
                    // const end_sell_time = end_sell_date.split("T")[1].slice(0, -1);
                    // const [end_hour, end_minute] = end_sell_time.split(":");
                    // this.stop_time = `${end_hour}:${end_minute}`;
                    const stop_date_temp = new Date(this.date.stop_date);
                    this.stop_date = stop_date_temp.toLocaleDateString();;
                    this.stop_time = stop_date_temp.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit', hour12: false});

                    //const [door_open_hour, door_open_minute] = this.date.door_open.split(':');
                    this.door_open = this.date.door_open;

                    //const [door_close_hour, door_close_minute] = this.date.door_close.split(':');
                    this.door_close = this.date.door_close;

                    //const [early_closure_hour, early_closure_minute] = this.date.early_closure_time.split(':');
                    this.early_closure_time = this.date.early_closure_time;
                    

                    


                    // Assign unique values to use as the pricing table column headers
                    this.columns = [...new Set(this.event.price_layer_price.map(x => x.price_type))];

                    // Assign unique values to use as the pricing table column rows
                    this.rows = [...new Set(this.event.price_layer_price.map(x => x.price_layer))];


                    this.initCalendar();


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
                            ['price'].forEach(key => value[object.price_type][key] = (value[object.price_type][key] + "," + object[key]).split(","));
                        } else {
                            value[object.price_type] = {
                                ...object
                            };
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
                    this.price_layer_sum = this.unique_prices.map(({
                        price
                    }) => price.reduce(sum));


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

                        



                    

                })
                .catch(error => {
                    console.log(error)
                })

            Promise.all([
                    axios.get('api/v1/facility/'),
                    axios.get('api/v1/location/'),
                    axios.get('api/v1/pricetype/'),
                    axios.get('api/v1/pricelayer/'),
                    axios.get('api/v1/account/')
                ])
                .then(([facilityResponse, locationResponse, pricetypeResponse, pricelayerResponse, accountResponse]) => {
                    this.all_facilities = facilityResponse.data.reverse();
                    this.all_locations = locationResponse.data.reverse();
                    this.all_pricetypes = pricetypeResponse.data.reverse();
                    this.all_pricelayers = pricelayerResponse.data.reverse();
                    this.all_accounts = accountResponse.data.reverse();
                })
                .catch(error => {
                    console.log(error);
                });

            this.$store.commit('setIsLoading', false)
        },


        initCalendar() {
            this.calendar1 = bulmaCalendar.attach(this.$refs.calendarTrigger1, {
                startDate: this.event_date,
            })[0];
            this.calendar1.on('select', e => {
                this.event_date = e.data.datePicker._date.start ? e.data.datePicker._date.start.toISOString().split('T')[0] : null;

                console.log(this.event_date);
            });

            this.calendar2 = bulmaCalendar.attach(this.$refs.calendarTrigger2, {
                startTime: this.event_time,
            })[0];
            this.calendar2.on('select', e => {
                this.event_time = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;

                console.log(this.event_time);
            });

            this.calendar3 = bulmaCalendar.attach(this.$refs.calendarTrigger3, {
                startTime: this.event_end_time,
            })[0];
            this.calendar3.on('select', e => {
                this.event_end_time = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                console.log(this.event_end_time);
            });

            this.calendar4 = bulmaCalendar.attach(this.$refs.calendarTrigger4, {
                startDate: this.sell_date,
                startTime: this.sell_time,
                //startTime: this.sell_time,
            })[0];
            this.calendar4.on('select', e => {
                const date = e.data.datePicker._date.start ? e.data.datePicker._date.start.toISOString().split('T')[0] : null;
                const time = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                const datetime = date && time ? `${date} ${time}` : null;
                this.sell_date = datetime;
                console.log(this.sell_date);
            });

            this.calendar5 = bulmaCalendar.attach(this.$refs.calendarTrigger5, {
                startDate: this.stop_date,
                startTime: this.stop_time,

                //startTime: this.stop_time,
            })[0];
            this.calendar5.on('select', e => {
                const date = e.data.datePicker._date.start ? e.data.datePicker._date.start.toISOString().split('T')[0] : null;
                const time = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                const datetime = date && time ? `${date} ${time}` : null;
                this.stop_date = datetime;
                console.log(this.stop_date);
            });

            this.calendar6 = bulmaCalendar.attach(this.$refs.calendarTrigger6, {
                startTime: this.door_open,
            })[0];
            this.calendar6.on('select', e => {
                this.door_open = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                console.log(this.door_open);
            });

            this.calendar7 = bulmaCalendar.attach(this.$refs.calendarTrigger7, {
                startTime: this.door_close,
            })[0];
            this.calendar7.on('select', e => {
                this.door_close = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                console.log(this.door_close);
            });

            this.calendar8 = bulmaCalendar.attach(this.$refs.calendarTrigger8, {
                startTime: this.early_closure_time,
            })[0];
            this.calendar8.on('select', e => {
                this.early_closure_time = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                console.log(this.early_closure_time);
            });
        },


        async submitForm() {
            this.$store.commit('setIsLoading', true)
            // validate capacity and held values
     if (this.capacity_held_total.capacity !== this.event.capacity ||
      this.capacity_held_total.held !== this.event.held) {
    try {
      this.showError = true;
    } catch (error) {
      // display error message in UI
      console.error(error.message);
    }
  } else {
            const payload = {
                name: this.event.name,
                description: this.event.description,
                location: this.event.location,
                facility: this.event.facility,
                capacity: this.event.capacity,
                held: this.event.held,
                entrance: this.event.entrance,
                gr_required: this.event.gr_required,
                early_closure: this.event.early_closure,
                csi_needed: this.event.csi_needed,
                csi_mandatory: this.event.csi_mandatory,
                csi_notes: this.event.csi_notes,
                additional_notes: this.event.additional_notes,
                website_link: this.event.website_link,
                websales_link: this.event.websales_link,
                date_time: {"event_date": this.event_date,
                            "event_time": this.event_time,
                            "event_end_time": this.event_end_time,
                            "sell_date": this.sell_date.includes(":") ? this.sell_date : this.date.sell_date,
                            "stop_date": this.stop_date.includes(":") ? this.stop_date : this.date.stop_date,
                            "door_open": this.door_open,
                            "door_close": this.door_close,
                            "early_closure_time": this.early_closure_time,},
                timeslot_set: this.time_slots, 
                price_layer_price: this.new_price_layer_price,

                discount: this.event.discount.map(obj => {
                            return {
                                price_type: { name: obj.price_type },
                                discount: obj.discount,
                                description: obj.description
                            };
                            }),


                account: this.event.account.map(item => {
                    return {
                    id: item.id,
                        account_data: {
                        gl_account: item.account_data.gl_account
                        },
                        price_layer: {
                        name: item.price_layer
                        }
                    };
                    }),

            }
            console.log(JSON.stringify(payload));
            this.$store.commit('setIsLoading', true);
            await axios
                
                .patch(`/api/v1/editevent/${this.$route.params.id}/`, payload)
                .then(response => {
                    console.log(response)
                    this.$store.commit('setIsLoading', false)
                    this.$router.push(this.$router.go())
                    
                })
                .catch(error => {
                    console.log(error)
                    this.$store.commit('setIsLoading', false)
                })
            
             }
        },
    },


}
</script>

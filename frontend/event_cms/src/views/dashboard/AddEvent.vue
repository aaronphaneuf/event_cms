<template>
  <div class="container">
   <section class="hero">
    <div class="hero-body">
     <div class="hero-overlay"></div>
      <p class="title">
       Create a New Event
      </p>
       <form @submit.prevent="submitForm" class="mb-4">
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
              <input type="text" class="input" v-model="name">
            </div>
          </div>
          <div class="field">
            <label>Description</label>
            <div class="control">
              <textarea class="textarea" v-model="description"></textarea>
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
                                <select v-model="location">
                                    <option v-for="location in all_locations" :value="location.id">
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
                                <select v-model="facility">
                                    <option v-for="facility in all_facilities" :value="facility.id">
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
                                <select v-model="entrance">
                                    <option>North Entrance</option>
                                    <option>South Entrance</option>
                                    <option>West Entrance</option>
                                </select>
                            </div>
                        </div>
                     
                    </div>
                    
                    <div class="field">
                        <label>Capacity</label>
                        <input class="input" type="number" v-model="capacity">
                    </div>
                    <div class="field">
                        <label>Held</label>
                        <input class="input" type="number" v-model="held">
                    </div>
                    <div class="field">
                    <label>GR Required</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="gr_required">
                                    <option>Yes</option>
                                    <option>No</option>
                                </select>
                            </div>
                        </div>
                    <label>Early Closure</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="early_closure">
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
                    <input type="text" data-type="time" v-model="event_time" ref="calendarTrigger2">
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
                            <tr v-for="slot in time_slots">
                                <td>
                                    <div class="select">
                                        <select v-model="slot.time_range">
                                            <option>{{slot.time_range}}</option>
                                            <option v-for="choice in time_slot_choices">{{choice}}</option>
                                        </select>
                                    </div>
                                </td>
                                <td><input type="number" class="input" v-model="slot.capacity"></td>
                                <td><input type="number" class="input" v-model="slot.held"></td>
                            </tr>
                            
                            
                            
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
                                    <th v-for="(column, columnIndex) in columns" :key="columnIndex">{{column}}</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(record, rowIndex) in records" :key="rowIndex">
                                    <td>{{record.name ? record.name : record.row}}</td>
                                    <td v-for="(detail, index) in record.details" :key="index">
                                        <input type="number" class="input" v-model="detail.value">
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
                                    <option v-for="name in all_price_layers" :key="name" :value="name">{{ name }}</option>
                                </select>
                            </div>
                            <div style="display: inline-block;">
                                <button @click="addRow" class="button is-primary is-small">Add Price Layer</button>
                            </div>
                            <div class="select" style="display: inline-block; vertical-align: middle;">
                                <select v-model="selectedColumn">
                                    <option v-for="name in all_price_types" :key="name" :value="name">{{ name }}</option>
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
                            </tr>
                        </thead>
                        <tbody>
                        <tr v-for="slot in discounts">
                                <td>
                                    <div class="select">
                                       <select v-model="slot.price_type">
                                            <option>{{slot.price_type}}</option>
                                        
                                             <option v-for="name in all_price_types" :key="name" :value="name">{{ name }}</option>
                                        </select>
                                    </div>
                                </td>
                                <td><input type="text" class="input" v-model="slot.discount"></td>
                                <td><input type="text" class="input" v-model="slot.description"></td>
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
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="acc in account">
                                <td><div class="select">
                                        <select v-model="acc.price_layer">
                                            <option>{{acc.price_layer}}</option>
                                            <option v-for="choice in all_price_layers">{{choice}}</option>
                                        </select>
                                    </div></td>
                                <td><div class="select">
                                <select v-model="acc.account.gl_account">
                                    <option v-if="acc.account">{{acc.account.gl_account}}</option>
                                    <option v-for="choice in all_accounts">{{choice.gl_account}}</option>
                                </select>
                                </div></td>
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
                            <tr><td>
                                <div class="select">
                                <select v-model="csi_needed">
                                    <option>Yes</option>
                                    <option>No</option>
                                </select>
                                </div></td>
                                <td>
                                <div class="select">
                                <select v-model="csi_mandatory">
                                    <option>Yes</option>
                                    <option>No</option>
                                </select>
                                </div></td>
                                <td><div class="control">
                                <input type="text" class="input" v-model="csi_notes">
                            </div></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="column is-12">
                <div class="box">
                    <h2 class="subtitle">Additional Notes</h2>
                    <div class="control">
                                <textarea class="textarea" v-model="additional_notes"></textarea>
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
                                <input type="text" class="input" v-model="website_link">
                            </td>
                            </tr>
                            <tr>
                                <td>Websales:</td>
                                <td><input type="text" class="input" v-model="websales_link"></td>
                            </tr>
                        </tbody>
                    </table>

                    
                </div>

                 <form @submit.prevent="submitForm" class="mb-4">
          <div class="field">
            <div class="control">
              <button class="button is-primary">Submit</button>
            </div>
          </div>
        </form>
            </div>
  </div>

  


            
        </div>
</template>


<script>
import axios from 'axios'
import bulmaCalendar from '../../../node_modules/bulma-calendar/dist/js/bulma-calendar.min.js'

export default {
  name: 'Events',
  data() {
    return {
      name: '',
      description: '',
      location: '',
      facility: '',
      capacity: '',
      held: '',
      entrance: '',
      gr_required: '',
      early_closure: '',
      csi_needed: '',
      csi_mandatory: '',
      csi_notes: '',
      additional_notes: '',
      website_link: '',
      websales_link: '',
      event_date: '',
      event_time:  '',
      event_end_time: '',
      door_open:  '',
      door_close:  '',
      sell_date:  '',
      sell_time: '',
      stop_date:  '',
      stop_time:  '',
      early_closure_time:  '',
      all_locations: [], // Added property for storing all locations
      all_facilities: [], // Added property for storing all facilities
      all_price_layers: [], // Added property for storing all price layers
      all_price_types: [], //Added property for storing all price types
      new_price_layer_price: [],
      columns: [],
      rows: [],
      records: [],
      time_slots: '',
      time_slot_choices: [    '6:00 - 6:30 AM',    '6:30 - 7:00 AM',    '7:00 - 7:30 AM',    '7:30 - 8:00 AM',    '8:00 - 8:30 AM',    '8:30 - 9:00 AM',    '9:00 - 9:30 AM',    '9:30 - 10:00 AM',    '10:00 - 10:30 AM',    '10:30 - 11:00 AM',    '11:00 - 11:30 AM',    '11:30 - 12:00 PM',    '12:00 - 12:30 PM',    '12:30 - 1:00 PM',    '1:00 - 1:30 PM',    '1:30 - 2:00 PM',    '2:00 - 2:30 PM',    '2:30 - 3:00 PM',    '3:00 - 3:30 PM',    '3:30 - 4:00 PM',    '4:00 - 4:30 PM',    '4:30 - 5:00 PM',    '5:00 - 5:30 PM',    '5:30 - 6:00 PM',    '6:00 - 6:30 PM',    '6:30 - 7:00 PM',    '7:00 - 7:30 PM',    '7:30 - 8:00 PM',    '8:00 - 8:30 PM',    '8:30 - 9:00 PM',    '9:00 - 9:30 PM',    '9:30 - 10:00 PM',    '10:00 - 10:30 PM',    '10:30 - 11:00 PM',    '11:00 - 11:30 PM',    '11:30 - 12:00 AM',    '12:00 - 12:30 AM'],
      capacity_held_total: { capacity: 0, held: 0 },

      selectedName: "",
      selectedColumn: "",


      discounts: [],

      account: [],
      all_accounts: null,

      
    }
  },
  mounted() {
    this.fetchLocations()
    this.fetchFacilities()
    this.fetchPriceLayers()
    this.fetchPriceTypes()
    this.fetchGLAccounts()
    this.initCalendar()
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

            


    },


    watch: { 
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
  


  
  
  methods: {
    async fetchLocations() {
      try {
        const response = await axios.get('api/v1/location/')
        this.all_locations = response.data
      } catch (error) {
        console.log(error)
      }
    },
    async fetchFacilities() {
      try {
        const response = await axios.get('api/v1/facility/')
        this.all_facilities = response.data
      } catch (error) {
        console.log(error)
      }
    },
    async fetchPriceLayers() {
      try {
        const response = await axios.get('api/v1/pricelayer/')
        this.all_price_layers = response.data
      } catch (error) {
        console.log(error)
      }
    },
    async fetchPriceTypes() {
      try {
        const response = await axios.get('api/v1/pricetype/')
        this.all_price_types = response.data
      } catch (error) {
        console.log(error)
      }
    },
    async fetchGLAccounts() {
      try {
        const response = await axios.get('api/v1/account/')
        this.all_accounts = response.data
      } catch (error) {
        console.log(error)
      }
    },

    addTimeSlot() {
      this.time_slots = [...this.time_slots, {
        time_range: '',
        capacity: 0,
        held: 0,
      }];
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


        // Button to add a discount
        addDiscount() {
            this.discounts.push({})
        },
        // Button to add a time slot

        // submit() {
        //     const data = {
        //         addTimeSlot: this.time_slots
        //     }
        //     alert(JSON.stringify(data, null, 2))
        // },

        addAccount() {
  this.account.push({
    account: { gl_account: ''},
    price_layer: ''
  });
},

    
    async submitForm() {
      
      this.$store.commit('setIsLoading', true)

      // Prepare the payload data for the new event
      const payload = {
        name: this.name,
        description: this.description,
        location: this.location,
        facility: this.facility,
        capacity: this.capacity,
        held: this.held,
        entrance: this.entrance,
        gr_required: this.gr_required,
        early_closure: this.early_closure,
        csi_needed: this.csi_needed,
        csi_mandatory: this.csi_mandatory,
        csi_notes: this.csi_notes,
        additional_notes: this.additional_notes,
        website_link: this.website_link,
        websales_link: this.websales_link,
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
        discount: this.discounts,
        account: this.account.map(item => {
                    return {
                        gl_account: {
                        gl_account: item.account.gl_account
                        },
                        price_layer: {
                        name: item.price_layer
                        }
                    };
                    }),
        csi_needed: this.csi_needed,
        csi_mandatory: this.csi_mandatory,
        csi_notes: this.csi_notes,
        additional_notes: this.additional_notes,
        websales_link: this.websales_link,
        website_link: this.website_link,
        

      };

        // Adjust 24:00 to 00:00 for sell_date
    if (payload.date_time.sell_date && payload.date_time.sell_date.includes(" 24:00")) {
    payload.date_time.sell_date = payload.date_time.sell_date.replace(" 24:00", " 00:00");
    }

    // Adjust 24:00 to 00:00 for stop_date
    if (payload.date_time.stop_date && payload.date_time.stop_date.includes(" 24:00")) {
    payload.date_time.stop_date = payload.date_time.stop_date.replace(" 24:00", " 00:00");
    }

      	const payload2 =  
	{"name":"Test Event 1",
	"description":"This is a test, so let's get lots of text here.",
		//"location":{ "location_name" : "Zoo Grounds"},
		//"facility":{ "facility_name" : "Zoo Events TT"},
	location: 1,
	facility: 1,
	"capacity":1000,
	"held":500,"entrance":
	"North Entrance",
	"gr_required":"No",
	"early_closure":"Yes",
	"csi_needed":"Yes",
	"csi_mandatory":"No",
	"csi_notes":"Team Name",
	"additional_notes":"asdfasdf",
	"website_link":"www.test1.com",
	"websales_link":"www.test2.com",
	"date_time":{"event_date":"2023-08-31","event_time":"18:00","event_end_time":"21:05","sell_date":"2023-07-13 01:00","stop_date":"2023-08-24 00:00","door_open":"18:00","door_close":"21:00","early_closure_time":"15:00"},
	"timeslot_set":[{"time_range":"6:00 - 6:30 PM","capacity":500,"held":250},{"time_range":"7:00 - 7:30 PM","capacity":500,"held":250}],
	"price_layer_price":[{"price":43,"price_layer":{"name":"Ticket Price"},"price_type":{"name":"Adult 18+"}},{"price":24,"price_layer":{"name":"Ticket Price"},"price_type":{"name":"Engage General"}},{"price":19,"price_layer":{"name":"Ticket Price"},"price_type":{"name":"Engage General"}},{"price":30,"price_layer":{"name":"Food"},"price_type":{"name":"Adult 18+"}},{"price":30,"price_layer":{"name":"Food"},"price_type":{"name":"Engage General"}},{"price":30,"price_layer":{"name":"Food"},"price_type":{"name":"Engage General"}}],
	


    "account":[{"gl_account":{"gl_account":"01-43000-1223"},"price_layer":{"name":"Ticket Price"}}],

    "discount":[{"price_type": "Adult 18+","discount":"29% off","description":"2 tickets", "hey": 99} ],}
     

    

    // Delete these two blocks later along with payload2
     // Adjust 24:00 to 00:00 for sell_date
     //if (payload2.date_time.sell_date && payload2.date_time.sell_date.includes(" 24:00")) {
     //payload2.date_time.sell_date = payload2.date_time.sell_date.replace(" 24:00", " 00:00");
     //}

     // Adjust 24:00 to 00:00 for stop_date
     //if (payload2.date_time.stop_date && payload2.date_time.stop_date.includes(" 24:00")) {
     //payload2.date_time.stop_date = payload2.date_time.stop_date.replace(" 24:00", " 00:00");
     //}  

      try {
        console.log(JSON.stringify(payload));
        await axios.post('api/v1/addevent/', payload)
        // Handle the success case
        console.log('Event added successfully!')
        this.$store.commit('setIsLoading', false)
      } catch (error) {
        // Handle the error case
        console.log(error)
        this.$store.commit('setIsLoading', false)
      }

      
    },

    initCalendar() {
            this.calendar1 = bulmaCalendar.attach(this.$refs.calendarTrigger1)[0];
            this.calendar1.on('select', e => {
                this.event_date = e.data.datePicker._date.start ? e.data.datePicker._date.start.toISOString().split('T')[0] : null;

                console.log(this.event_date);
            });

            this.calendar2 = bulmaCalendar.attach(this.$refs.calendarTrigger2)[0];
            this.calendar2.on('select', e => {
                this.event_time = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;

                console.log(this.event_time);
            });

            this.calendar3 = bulmaCalendar.attach(this.$refs.calendarTrigger3)[0];
            this.calendar3.on('select', e => {
                this.event_end_time = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                console.log(this.event_end_time);
            });

            this.calendar4 = bulmaCalendar.attach(this.$refs.calendarTrigger4)[0];
            this.calendar4.on('select', e => {
                const date = e.data.datePicker._date.start ? e.data.datePicker._date.start.toISOString().split('T')[0] : null;
                const time = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                const datetime = date && time ? `${date} ${time}` : null;
                this.sell_date = datetime;
                console.log(this.sell_date);
            });

            this.calendar5 = bulmaCalendar.attach(this.$refs.calendarTrigger5)[0];
            this.calendar5.on('select', e => {
                const date = e.data.datePicker._date.start ? e.data.datePicker._date.start.toISOString().split('T')[0] : null;
                const time = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                const datetime = date && time ? `${date} ${time}` : null;
                this.stop_date = datetime;
                console.log(this.stop_date);
            });

            this.calendar6 = bulmaCalendar.attach(this.$refs.calendarTrigger6)[0];
            this.calendar6.on('select', e => {
                this.door_open = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                console.log(this.door_open);
            });

            this.calendar7 = bulmaCalendar.attach(this.$refs.calendarTrigger7)[0];
            this.calendar7.on('select', e => {
                this.door_close = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                console.log(this.door_close);
            });

            this.calendar8 = bulmaCalendar.attach(this.$refs.calendarTrigger8)[0];
            this.calendar8.on('select', e => {
                this.early_closure_time = e.data.timePicker._time.start ? new Date(e.data.timePicker._time.start).toLocaleTimeString('en-US', {hour12: false, hour: '2-digit', minute: '2-digit'}) : null;
                console.log(this.early_closure_time);
            });
  

  
},


  }
}
</script>

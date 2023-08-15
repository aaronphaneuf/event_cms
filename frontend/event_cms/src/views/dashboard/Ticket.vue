<template>
  <div class="container">
    <section class="hero">
      <div class="hero-body">
        <div class="hero-overlay"></div>
        <h1 class="title">Print at Home Ticket</h1>
        <div class="field is-grouped"></div>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <div class="box">
          <div class="column is-12">
            <div class="table-container">
                <table class="table is-fullwidth">
                  <tbody>
                    <tr>
                      <td colspan="2">
                        <div class="columns is-vcentered">
  <div class="column is-narrow">
    <strong class="ticket-label">This is your ticket for:</strong>
  </div>
  <div class="column">
    <div class="field">
      <div class="control">
        <input class="input is-fullwidth" v-model="ticket.name" type="text" placeholder="Enter ticket number">
      </div>
    </div>
  </div>
</div>
                      </td>
                      <td></td>
                    </tr>
                    <tr>
    <td>
      <div class="columns is-vcentered">
        <div class="column">
          <strong>Date:</strong>
        </div>
        <div class="column">
          <div class="field">
            <div class="control">
              <input class="input" v-model="ticket.date" type="text" placeholder="Enter date">
            </div>
          </div>
        </div>
      </div>
    </td>
    <td>
      <div class="columns is-vcentered">
        <div class="column">
          <strong>Time:</strong>
        </div>
        <div class="column">
          <div class="field">
            <div class="control">
              <input class="input" v-model="ticket.time" type="text" placeholder="Enter date">
            </div>
          </div>
        </div>
      </div>
    </td>
    </tr>
    <tr>
     <td>
      <div class="columns is-vcentered">
        <div class="column">
          <strong>Price Type:</strong>
        </div>
        <div class="column">
          <div class="field">
            <div class="control">
              <input class="input" v-model="ticket.ticket_type" type="text" placeholder="Enter date">
            </div>
          </div>
        </div>
      </div>
    </td>
    <td>
      <div class="columns is-vcentered">
        <div class="column">
          <strong>Price:</strong>
        </div>
        <div class="column">
          <div class="field">
            <div class="control">
              <input class="input" v-model="ticket.price" type="text" placeholder="Enter date">
            </div>
          </div>
        </div>
      </div>
    </td>
    </tr>
    <tr>
     <td>
      <div class="columns is-vcentered">
        <div class="column">
          <strong>Order Date:</strong>
        </div>
        <div class="column">
          <div class="field">
            <div class="control">
              <input class="input" v-model="ticket.order_date" type="text" placeholder="Enter date">
            </div>
          </div>
        </div>
      </div>
    </td>
    <td>
      <div class="columns is-vcentered">
        <div class="column">
          <strong>Order Number:</strong>
        </div>
        <div class="column">
          <div class="field">
            <div class="control">
              <input class="input" v-model="ticket.order_number" type="text" placeholder="Enter date">
            </div>
          </div>
        </div>
      </div>
    </td>
    </tr>
    <tr>
     <td>
      <div class="columns is-vcentered">
        <div class="column">
          <strong>Location:</strong>
        </div>
        <div class="column">
          <div class="field">
            <div class="control">
              <input class="input" v-model="ticket.location" type="text" placeholder="Enter date">
            </div>
          </div>
        </div>
      </div>
    </td>
    <td>
      <div class="columns is-vcentered">
        <div class="column">
          <strong>Custom:</strong>
        </div>
        <div class="column">
          <div class="field">
            <div class="control">
              <input class="input" v-model="ticket.custom_1" type="text" placeholder="Enter date">
            </div>
          </div>
        </div>
      </div>
    </td>
    </tr>


    <tr>
                      <td colspan="2">
                        <div class="columns is-vcentered">
  <div class="column is-narrow">
    <strong class="ticket-label">Barcode:</strong>
  </div>
  <div class="column">
    <div class="field">
      <div class="control">
        <input class="input is-fullwidth" v-model="ticket.barcode" type="number" placeholder="Enter ticket number">
      </div>
    </div>
  </div>
</div>
                      </td>
                      <td></td>
                    </tr>
    <tr>





    <td colspan="2">
    <div class="column">
  <strong>Text Field 1:</strong>
</div>
<div class="column">
  <div class="field">
    <div class="control">
      <textarea class="textarea" v-model="ticket.text_field_1" placeholder="Enter text"></textarea>
    </div>
  </div>
</div>
</td>
    </tr>
    <tr>
    <td colspan="2">
    <div class="column">
  <strong>Text Field 2:</strong>
</div>
<div class="column">
  <div class="field">
    <div class="control">
      <textarea class="textarea" v-model="ticket.text_field_2" placeholder="Enter text"></textarea>
    </div>
  </div>
</div>
</td>
    </tr>
    <tr>
    <td colspan="2">
    <div class="column">
  <strong>Text Field 3:</strong>
</div>
<div class="column">
  <div class="field">
    <div class="control">
      <textarea class="textarea" v-model="ticket.text_field_3" placeholder="Enter text"></textarea>
    </div>
  </div>
</div>
</td>
    </tr>

    <tr>
    <td colspan="2">
    <div class="column">
  <strong>Text Field 4:</strong>
</div>
<div class="column">
  <div class="field">
    <div class="control">
      <textarea class="textarea" v-model="ticket.text_field_4" placeholder="Enter text"></textarea>
    </div>
  </div>
</div>
</td>
    </tr>

    <tr>
    <td colspan="2">
    <div class="column">
  <strong>Text Field 5:</strong>
</div>
<div class="column">
  <div class="field">
    <div class="control">
      <textarea class="textarea" v-model="ticket.text_field_5" placeholder="Enter text"></textarea>
    </div>
  </div>
</div>
</td>
    </tr>






                  </tbody>
                </table>
              </div>
            </div>
          </div>


          <button class="button is-primary" @click="downloadPdf">Download PDF</button>

          <form @submit.prevent="submitForm" class="mb-4">
        <div class="field">
         <div class="control">
          <button class="button is-primary">Save Ticket</button>
         </div>
        </div>
       </form>
        </div>
      </div>
  
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ticket',
  data() {
    return {
      ticket: {
        
        //event_name: '',
        //date: '',
        //time: '',
        //price_type: '',
        //price: '',
        //order_number: '',
        //order_date: '',
        //text_field_1: ''
      }
    };
  },
  created() {
    this.fetchTicket();
  },
  methods: {
    fetchTicket() {
  axios.get(`http://localhost:8000/api/v1/ticket_detail/${this.$route.params.id}`)
    .then(response => {
      this.ticket = response.data;
    })
    .catch(error => {
      console.error(error);
    });
},
async submitForm() {
      
      this.$store.commit('setIsLoading', true)
const payload = this.ticket
try {
        
        await axios.put('http://localhost:8000/api/v1/ticket/1/', payload)
        // Handle the success case
        this.$store.commit('setIsLoading', false)
        this.$router.push(this.$router.go())
      } catch (error) {
        // Handle the error case
        this.$store.commit('setIsLoading', false)
      }
},


    downloadPdf() {
      axios({
        method: 'get',
        url: `http://localhost:8000/api/v1/ticket_view/${this.$route.params.id}`,
        responseType: 'blob',
        params: this.ticket
      })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', 'PAHT.pdf');
          document.body.appendChild(link);
          link.click();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

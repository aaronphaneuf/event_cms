// Leads.vue

<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <form @submit.prevent="submitForm" class="mb-4">
          <div class="field">
            <div class="control">
              <button class="button is-primary">Submit</button>
            </div>
          </div>
        </form>
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
                                <select v-model="facility">
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
        </div>
</template>


<script>
import axios from 'axios'

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
      all_locations: [], // Added property for storing all locations
      all_facilities: [], // Added property for storing all facilities
    }
  },
  mounted() {
    this.fetchLocations()
    this.fetchFacilities()
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
    async addEvent() {
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
        // Example: title, description, date, etc.
      }

      try {
        await axios.post('api/v1/events/', payload)
        // Handle the success case
        console.log('Event added successfully!')
        this.$store.commit('setIsLoading', false)
      } catch (error) {
        // Handle the error case
        console.log(error)
        this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>

<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Game</th>
                            <th>Played On</th>
                        </tr>
                    </thead>
                    <tbody>
                    <!-- For each game, display the id with a router link, as well as the date played !-->
                        
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default { 
        name: 'Games',
        data() { 
            return { 
                game: [],
                fact: [],
            }
        },
        mounted() { 
            this.getGame()
        },
        methods: { 
            async getGame() { 
                this.$store.commit('setIsLoading', true)
                const EventID = this.$route.params.id
                axios
                    .get('/api/v1/events/')
                    .then(response => { 
                        this.game = response.data.reverse()
                    })
                    .catch(error => { 
                        console.log(error)
                    })
               
                axios
                    .get('api/v1/facility/')
                    .then(response => { 
                        this.fact = response.data.reverse()
                    })
                    .catch(error => { 
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
        }
   
    }
</script>

    <template>
    <link rel="stylesheet" 
        href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" 
        integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" 
        crossorigin="anonymous">
        <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
                   <strong><i class="fa fa-calendar fa-2x" aria-hidden="true"></i> Event CMS </strong>
                </router-link>

        <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        </a>
    </div>

    <div class="navbar-menu">
                <div class="navbar-end">
                    <router-link to="/dashboard/events" class="navbar-item">Events</router-link>
                    
                        
                            <template v-if="!$store.state.isAuthenticated">
                                <router-link to="/sign-up" class="navbar-item"><strong>Sign Up</strong></router-link>
                                <router-link to="/log-in" class="navbar-item"><strong>Log in</strong></router-link>
                            </template>

                            <template v-else>
                                <router-link to="/dashboard/my-account" class="navbar-item">My Account</router-link>
                            </template>
                       
                   
                </div>
            </div>
    </nav>

</template>
<script>
    export default { 
        name: 'Navbar'
    }
</script>
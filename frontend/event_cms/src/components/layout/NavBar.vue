
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

       <a role="button" class="navbar-burger" data-target="navMenu" aria-label="menu" aria-expanded="false">
  <span aria-hidden="true"></span>
  <span aria-hidden="true"></span>
  <span aria-hidden="true"></span>
</a>

        
    </div>

    <div class="navbar-menu" id="navMenu">
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

    document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Add a click event on each of them
  $navbarBurgers.forEach( el => {
    el.addEventListener('click', () => {

      // Get the target from the "data-target" attribute
      const target = el.dataset.target;
      const $target = document.getElementById(target);

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');

    });
  });

});

</script>
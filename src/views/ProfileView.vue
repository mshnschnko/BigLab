<template>
  <v-app>
    <v-app-bar
        app
        color="white"
        flat
    >
      <v-container class="fill-height">
        <v-responsive max-width="260">
          <v-text-field
              dense
              flat
              hide-details
              rounded
              solo-inverted
              placeholder="Поиск..."
          ></v-text-field>
        </v-responsive>

        <v-spacer></v-spacer>

        <v-btn @click="$router.push({path: '/home'});">
          Главная
        </v-btn>
        <v-btn icon @click="$router.push({path: '/profile'});">
          <v-avatar
              color="grey darken-1"
              size="32"
          >
            <v-icon>mdi-account-circle</v-icon>
          </v-avatar>
        </v-btn>
        <v-btn
            icon
            @click="logout"
        >
          <v-icon> mdi-logout </v-icon>
        </v-btn>
      </v-container>
    </v-app-bar>
    <v-main class="grey lighten-3">
      <v-container>
        <v-col cols="12">
          <v-sheet min-height="85vh"
                   max-height="85vh"
                   class="overflow-y-auto rounded-lg">
            <v-row  class="align-content-center">
              <v-avatar
                  color="grey darken-1"
                  size="128"
              >
                <v-icon size="128">mdi-account-circle</v-icon>
              </v-avatar>
            </v-row>
          </v-sheet>
        </v-col>
      </v-container>
<!--      <v-banner>-->
<!--        {{ user.name }}-->
<!--      </v-banner>-->
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  name: "ProfileView",
  props: ['id'],
  data: () => ({
    user: {},
  }),
  created() {
    axios.get(`http://127.0.0.1:8000/backend_app/user?query=id&id=${this.$props.id}`)
        .then(response => {
          if (response.status === 200) {
            this.$data.user = response.data[0];
          }
        })
  }
}
</script>

<style scoped>

</style>
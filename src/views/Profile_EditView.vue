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
      <v-container class = "align-content-center">
        <v-avatar
            color = "grey lighten-1"
            size = "128"
        >
        </v-avatar>
        <v-dialog
            width="500"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn class = "ma-12"
                   v-bind="attrs"
                   v-on="on"
            >
              Изменить фотографию
            </v-btn>
          </template>
          <v-card>
            <v-card-title class="text-h5 grey lighten-2">
              Новое фото
            </v-card-title>

            <v-card-text>
              Вставьте ссылку на вашу фотографию
            </v-card-text>
            <v-col>
              <v-text-field
                  placeholder = "URL"
              >
              </v-text-field>
            </v-col>

            <v-divider></v-divider>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                  color="primary"
                  text
              >
                Сохранить
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-text-field
            v-model = "user.name"
        >
        </v-text-field>
        <v-text-field
            v-model = "user.email"
        >
        </v-text-field>
        <v-btn>
          Сохранить
        </v-btn>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  name: "Profile_EditView",
  components: {},

  props: ['id'],
  data: () => ({
    user: {},
  }),
  mounted() {
    axios.get(`http://127.0.0.1:8000/backend_app/user?query=id&id=${localStorage.userid}`)
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

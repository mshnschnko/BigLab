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
        <v-avatar color = "grey lighten-1"
                  size = "128"
        >
        </v-avatar>
        <v-banner>
          {{ user.name }}
        </v-banner>
        <v-banner>
          {{ user.email }}
        </v-banner>
        <v-btn @click = "$router.push({path: '/profile_edit'});"
               v-if="user.id == current_id"
        >
          Изменить профиль
        </v-btn>
        <v-btn @click = "relationship"
               v-if="user.id != current_id &&
               user.profile_type != current_profile_type &&
               user.profile_type != 1 &&
               current_profile_type != 1 &&
               relations === false"
        >
          Завести денежные отношения
        </v-btn>
        <v-dialog>
          <v-card v-if="relation_error === true">
            <v-card-title>
              Не удалось завести денежные отношения. Попробуйте позже.
            </v-card-title>
          </v-card>
        </v-dialog>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  name: "ProfileView",
  components: {},

  props: ['id'],
  data: () => ({
    relations: true,
    relation_error: false,
    tmp_data: {},
    user: {},
    current_id: {},
    current_profile_type: {},
  }),
  created() {
    // let getData = async () => {
    //   let response = await axios.get(`http://127.0.0.1:8000/backend_app/user?query=id&id=${this.$props.id}`)
    //       // .then(response => {
    //       //   if (response.status === 200) {
    //       //     console.log(response.data[0]);
    //       //     this.$data.user = response.data[0];
    //       //   }
    //       // })
    //   this.$data.user = response;
    // };
    // getData();
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/backend_app/user?query=id&id=${this.$props.id}`)
        .then(response => {
          if (response.status === 200) {
            console.log(response.data[0]);
            this.$data.user = response.data[0];
          }
        })
    console.log(this.$props.id);
    console.log(this.$data.user.name);
    this.$data.current_id = localStorage.userid;
    this.$data.current_profile_type = localStorage.profile_type;
    setTimeout(() => {
      if (this.$data.user.profile_type == 2) {
        axios.get(`http://127.0.0.1:8000/backend_app/pairs?studid=${this.$data.user.id}&tutorid=${this.$data.current_id}`)
            .then(response => {
              if (response.status === 200) {
                if (response.data[0] !== undefined) {
                  this.$data.relations = true;
                }
                else {
                  this.$data.relations = false;
                }
              }
            })
            .catch(error => {
              console.log(error);
              this.$data.relations = false;
            })
      }
      else
        axios.get(`http://127.0.0.1:8000/backend_app/pairs?studid=${this.$data.current_id}&tutorid=${this.$data.user.id}`)
            .then(response => {
              if (response.status === 200) {
                if (response.data[0] !== undefined) {
                  this.$data.relations = true;
                } else {
                  this.$data.relations = false;
                }
              }
            })
            .catch(error => {
              console.log(error);
              this.$data.relations = false;
            })
    }, 1000)
    // if (this.$data.user.profile_type == 2) {
    //   axios.get(`http://127.0.0.1:8000/backend_app/pairs?studid=${this.$data.user.id}&tutorid=${this.$data.current_id}`)
    //       .then(response => {
    //         if (response.status === 200) {
    //           console.log(response.data);
    //           this.$data.relations = true;
    //         }
    //       });
    // }
    // else
    //   axios.get(`http://127.0.0.1:8000/backend_app/pairs?studid=${this.$data.current_id}&tutorid=${this.$data.user.id}`)
    //       .then(response => {
    //         if (response.status === 200) {
    //           this.$data.relations = true;
    //         }
    //       });
  },
  methods: {
    relationship () {
      let request = {};
      if (this.$data.user.profile_type == 2) {
        axios.get(`http://127.0.0.1:8000/backend_app/user?query=id&id=${this.$data.current_id}`)
            .then(response => {
              if (response.status === 200) {
                this.$data.tmp_data = response.data[0];
                console.log(this.$data.tmp_data.subject);
              }
            })
        request = {student_id: this.$data.user.id,
          teacher_id: this.$data.current_id,
          subject: this.$data.tmp_data.subject};
      }
      else {
        axios.get(`http://127.0.0.1:8000/backend_app/user?query=id&id=${this.$data.user.id}`)
            .then(response => {
              if (response.status === 200) {
                this.$data.tmp_data = response.data[0];
              }
            })
        request = {teacher_id: this.$data.user.id,
          student_id: this.$data.current_id,
          subject: this.$data.tmp_data.subject};
      }
      axios.post(`http://127.0.0.1:8000/backend_app/pairs`, request)
          .then(response =>{
            if (response.status === 201) {
              this.$data.relations = true;
            }
          })
          .catch(error =>{
            console.log(error);
            this.$data.relation_error = true;
          });
    },
    logout () {
      localStorage.removeItem('userid');
      localStorage.removeItem('profile_type');
      this.$router.push({path: '/login'});
    }
  }
}
</script>

<style scoped>

</style>
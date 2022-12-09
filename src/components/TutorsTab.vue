<template>
  <div>
    <v-sheet
        min-height="80vh"
        max-height="80vh"
        class="overflow-y-auto rounded-lg">
      <v-toolbar
          flat
          class="rounded-lg rounded-b-0"
      >
        <v-tabs>
          <v-tab class="ma-2"
                 text
          >Математика
          </v-tab>
          <v-tab class="ma-2"
                 text
          >Физика
          </v-tab>
        </v-tabs>
      </v-toolbar>

      <v-divider></v-divider>

      <v-sheet>
        <v-list
            class="rounded-lg rounded-t-0"
            v-for="tutor in tutors"
            :key="tutor"
        >
          <v-list-item link>
            <v-list-item-content>
              <v-list-item-title>{{ tutor }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-sheet>
    </v-sheet>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "TutorsTab",
  data: () => ({
    tutors: [],
  }),
  beforeCreate() {
    let request = {};
    axios.get(`http://127.0.0.1:8000/backend_app/getuser/?query=profile&type=3`, request)
        .then(response => {
          if (response.status === 200) {
            let i;
            for (i = 0; i < response.data.length; i++) {
              this.$data.tutors.push(response.data[i].name);
            }
          }
        })
        .catch(error => {
          console.log(error);
        })
  }
}

</script>

<style scoped>

</style>
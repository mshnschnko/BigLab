<template>
  <div>
    <v-row>
      <v-col cols="3">
        <v-sheet
            class="overflow-y-auto rounded-l-lg"
            min-height="85vh"
            max-height="85vh"
        >
          <v-list
              class="rounded-l-lg"
              v-for="tutor in tutors"
              :key="tutor"
          >
            <v-list-item
                link
                class="v-list-item--two-line"
                @click="subpage=tutor.name"
            >
              <v-avatar color="grey darken-1" size="32">
                <v-icon>mdi-account-circle</v-icon>
              </v-avatar>
              <v-list-item-content class="ml-3">
                <v-list-item-title>
                  {{ tutor.name }}
                </v-list-item-title>
                <v-list-item-subtitle>
                  Some Text...
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
            <v-divider class="text-grey-lighten-1"></v-divider>
          </v-list>
          <!--  -->
        </v-sheet>
      </v-col>
      <v-col cols="9">
        <v-sheet
            min-height="85vh"
            max-height="85vh"
            class="rounded-r-lg overflow-y-auto"
        >
          <v-divider style="position: relative; top: 78vh" v-if="subpage!=='none'"></v-divider>
          <v-container style="position: relative; padding-top: 78.5vh" v-if="subpage!=='none'">
            <v-responsive width="85vh" style="position: absolute; left: 5px">
              <v-text-field
                  dense
                  flat
                  hide-details
                  solo-inverted
                  class="rounded-lg"
              ></v-text-field>
            </v-responsive>
            <v-icon
                large
                style="position: absolute; right: 10px"
                @click=";"
            >
              mdi-send
            </v-icon>
          </v-container>
        </v-sheet>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MessagesTab",
  data: () => ({
    tutors: [],
    subjects: [],
    subpage: 'none',
  }),
  mounted() {
    axios.get(`http://127.0.0.1:8000/backend_app/subject`)
        .then(response => {
          console.log(response.data);
          if (response.status === 200) {
            let i;
            for (i = 0; i < response.data.length; i++) {
              console.log(response.data[i].subject);
              this.$data.subjects.push(response.data[i].subject);
            }
          }
        })
        .catch(error => {
          console.log(error);
        });
    let request = {};
    let queryparam = ``;
    // axios.get(`http://127.0.0.1:8000/backend_app/user?query=profile&type=3`, request)
    if (localStorage.userid && localStorage.profile_type) {
      if (localStorage.profile_type === '2') {
        queryparam = `studid=${localStorage.userid}`;
      }
      else if (localStorage.profile_type === '3') {
        queryparam = `tutorid=${localStorage.userid}`;
      }
      console.log(`http://127.0.0.1:8000/backend_app/pairs?${queryparam}`);
      axios.get(`http://127.0.0.1:8000/backend_app/pairs?${queryparam}`, request)
          .then(response => {
            if (response.status === 200) {
              let i;
              for (i = 0; i < response.data.length; i++) {
                if (localStorage.profile_type === '2') {
                  console.log(response.data[i].teacher_id);
                  axios.get(`http://127.0.0.1:8000/backend_app/user?query=id&id=${response.data[i].teacher_id}`)
                      .then(response => {
                        if (response.status === 200) {
                          this.$data.tutors.push(response.data[0]);
                        }
                      })
                      .catch(error => {
                        console.log(error);
                      })
                }
                else if (localStorage.profile_type === '3') {
                  axios.get(`http://127.0.0.1:8000/backend_app/user?query=id&id=${response.data[i].student_id}`)
                      .then(response => {
                        if (response.status === 200) {
                          this.$data.tutors.push(response.data[0]);
                        }
                      })
                      .catch(error => {
                        console.log(error);
                      })
                }
                // this.$data.tutors.push(response.data[i].teacher_id);
              }
            }
          })
          .catch(error => {
            console.log(error);
          })
    }
  }
}
</script>

<style scoped>

</style>
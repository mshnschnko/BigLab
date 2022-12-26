<template>
  <div>
    <v-sheet
        min-height="85vh"
        max-height="85vh"
        class="overflow-y-auto rounded-lg">
<!--      <v-toolbar-->
<!--          flat-->
<!--          class="rounded-lg rounded-b-0"-->
<!--      >-->
<!--        <v-tabs>-->
<!--          <v-tab class="ma-2"-->
<!--                 text-->
<!--          >Математика-->
<!--          </v-tab>-->
<!--          <v-tab class="ma-2"-->
<!--                 text-->
<!--          >Физика-->
<!--          </v-tab>-->
<!--        </v-tabs>-->
<!--      </v-toolbar>-->

<!--      <v-divider></v-divider>-->

      <v-sheet>
        <v-banner
            v-if="tutors.length === 0"
            class="align-self-center align-content-center justify-lg-center"
        >
          Нет активных договоров
        </v-banner>
        <v-list
            class="rounded-lg rounded-t-0"
            v-for="tutor in tutors"
            :key="tutor"
        >
          <v-list-item
              link
              @click="$router.push({path: `/profile/${tutor.id}`})"
          >
            <v-avatar
                class="mr-2"
                color="grey darken-1"
                size="32">
              <v-icon>mdi-account-circle</v-icon>
            </v-avatar>
            <v-list-item-content>
              <v-list-item-title>{{ tutor.name }}</v-list-item-title>
              <v-list-item-subtitle>{{ subjects[tutor.subject-1] }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-divider/>
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
    subjects: [],
  }),
  // beforeCreate() {
  //   axios.get(`http://127.0.0.1:8000/backend_app/subject`)
  //       .then(response => {
  //         if (response.status === 200) {
  //           let i;
  //           for (i = 0; i < response.data.length; i++) {
  //             this.$data.subjects.push(response.data[i].subject);
  //           }
  //         }
  //       })
  //       .catch(error => {
  //         console.log(error);
  //       })
  // },
  created() {
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
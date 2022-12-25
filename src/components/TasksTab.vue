<template>
  <div>
    <v-sheet class="rounded-lg">
      <v-toolbar
          flat
          class="rounded-lg rounded-b-0"
      >
        <v-tabs>
          <v-tab class="ma-2"
                 text
          >Назначено
          </v-tab>
          <v-tab class="ma-2"
                 text
          >Выполнено
          </v-tab>
<!--          <v-col cols="3">-->
<!--            <v-select-->
<!--                clearable-->
<!--                :items="teachers"-->
<!--                label="Репетиторы"-->
<!--            ></v-select>-->
<!--          </v-col>-->
        </v-tabs>
      </v-toolbar>

      <v-divider></v-divider>

      <v-sheet
          min-height="85vh"
          max-height="85vh"
          class="overflow-y-auto rounded-lg rounded-t-0"
      >
        <v-col
            v-for="card in cards"
            :key="card"
            cols="12"
        >
          <v-card>
            <v-subheader>{{ card }}</v-subheader>

            <v-list two-line>
              <template v-for="task in tasks">
                <v-list-item
                    :key="task"
                    link
                    :href="task.link_to_task"
                >
                  <v-list-item-avatar color="grey darken-1">
                  </v-list-item-avatar>

                  <v-list-item-content>
                    <v-list-item-title>
                      {{task.link_to_task}}
                    </v-list-item-title>

                    <v-list-item-subtitle>
<!--                      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio-->
<!--                      similique-->
                      {{ task.task_comment }}
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>

                <v-divider
                    v-if="task !== tasks[tasks.length-1]"
                    :key="task"
                    inset
                ></v-divider>
              </template>
            </v-list>
          </v-card>
        </v-col>
      </v-sheet>
    </v-sheet>
  </div>
</template>

<script>
// import axios from "axios";
import axios from "axios";

export default {
  data: () => ({
    cards: ['Today', 'Yesterday'],
    drawer: null,
    sections: [
      'Задания'
    ],
    items: [
      {
        icon: 'mdi-pencil',
        text: 'Задания',
      },
    ],
    teachers: [
      'Victor Igorevich',
      'Vyacheslav Sergeevich'
    ],
    tasks: [],
    // teachers: [
    //   {
    //     name: 'Victor Igorevich',
    //   },
    //   {
    //     name: 'Vyacheslav Sergeevich'
    //   },
    // ],
    model: 1,
    variant: "default"
  }),
  mounted() {
    axios.get(`http://127.0.0.1:8000/backend_app/task?query=byuserid&id=${localStorage.userid}`)
        .then(response => {
          if (response.status === 200) {
            let i;
            for (i = 0; i < response.data.length; i++) {
              this.$data.tasks.push(response.data[i]);
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
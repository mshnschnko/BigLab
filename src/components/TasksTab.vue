<template>
  <div>
    <v-sheet class="rounded-lg" v-if="subpage === 'Tasks'">
      <v-toolbar
          flat
          class="rounded-lg rounded-b-0"
      >
        <v-tabs>
          <v-tab class="ma-2"
                 text
                 @click="sections = 'Назначено'"
          >Назначено
          </v-tab>
          <v-tab class="ma-2"
                 text
                 @click="sections = 'Выполнено'"
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
        <v-btn
            v-if="profile_type === '3'"
            class="mr-0"
            @click="subpage = 'Create Task'"
        >
          Создать
        </v-btn>
      </v-toolbar>

      <v-divider></v-divider>

      <v-sheet
          v-if="sections === 'Назначено'"
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
              <template v-for="task in assigned_tasks">
                <v-list-item
                    :key="task"
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
                    <v-btn
                        max-width="10vh"
                        min-width="10vh"
                        v-if="profile_type === '3'"
                        class="mr-0"
                        @click="acceptTask(task.id)"
                    >Зачесть</v-btn>
                  </v-list-item-content>
                </v-list-item>

                <v-divider
                    v-if="task !== assigned_tasks[assigned_tasks.length-1]"
                    :key="task"
                    inset
                ></v-divider>
              </template>
            </v-list>
          </v-card>
        </v-col>
      </v-sheet>

      <v-sheet
          v-if="sections === 'Выполнено'"
          min-height="85vh"
          max-height="85vh"
          class="overflow-y-auto rounded-lg rounded-t-0"
      >
        <v-col
            cols="12"
        >
          <v-card>
<!--            <v-subheader>{{ card }}</v-subheader>-->

            <v-list two-line>
              <template v-for="task in completed_tasks">
                <v-list-item
                    :key="task"
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
                    v-if="task !== completed_tasks[completed_tasks.length-1]"
                    :key="task"
                    inset
                ></v-divider>
              </template>
            </v-list>
          </v-card>
        </v-col>
      </v-sheet>
    </v-sheet>
    <v-sheet v-if="subpage === 'Create Task'">
      <v-toolbar
          flat
          class="rounded-lg rounded-b-0"
      >
        <v-btn
            class="mr-0"
            @click="subpage = 'Tasks'"
        >
          Назад
        </v-btn>
      </v-toolbar>

      <v-container>
        <v-text-field
            v-model="description"
            label="Описание"
        >
        </v-text-field>

        <v-text-field
            v-model="tasklink"
            label="Ссылка на задание"
            required>
        </v-text-field>
        <v-select
            v-model="choosenStudent"
            :items="students"
            item-text="name"
            item-value="id"
            :rules="[v => !!v || 'Необходимо выбрать получателя']"
            label="Студент"
            required
        >
        </v-select>
        <v-menu
            v-model="menu2"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
                v-model="date"
                label="Крайний срок сдачи"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
              v-model="date"
              @input="menu2 = false"
          ></v-date-picker>
        </v-menu>
        <v-btn
          class="mr-0"
          @click="CreateTask"
        >
          Отправить
        </v-btn>
      </v-container>
    </v-sheet>
  </div>
</template>

<script>
// import axios from "axios";
import axios from "axios";

export default {
  data: () => ({
    profile_type: '',
    subpage: 'Tasks',
    cards: ['Today', 'Yesterday'],
    drawer: null,
    sections: "Назначено",
    choosenStudent: 0,
    relationid: '',
    tasklink: '',
    description: '',
    mainsheet: 0,
    date: '',
    menu2: false,
    students: [],
      // ids:[],
      // names:[],
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
    completed_tasks: [],
    assigned_tasks: [],
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
  methods: {
    acceptTask(taskid) {
      let request = {
        id: taskid,
        new_status: "completed",
        completion_time: new Date().toISOString().split('.')[0]+"Z"
      };
      axios.patch(`http://127.0.0.1:8000/backend_app/task`, request)
      this.mainsheet += 1;
      window.location.reload();

    },
    printdd() {
      console.log(this.$data.choosenStudent, this.$data.date + 'T23:59:00Z', new Date().toISOString().split('.')[0]+"Z");
    },
    CreateTask() {
      axios.get(`http://127.0.0.1:8000/backend_app/pairs?tutorid=${localStorage.userid}&studid=${this.$data.choosenStudent.toString()}`)
          .then(response => {
            if (response.status === 200) {
              this.$data.relationid = response.data[0].id;
            }
          })
          .catch(error => {
            console.log("CAAATCH");
            console.log(error);
          })
      let request = {relation_id: this.$data.relationid.toString(),
        link_to_task: this.$data.tasklink,
        task_status: "assigned",
        task_comment: this.$data.description,
        publication_time: new Date().toISOString().split('.')[0]+"Z",
        deadline: this.$data.date + 'T23:59:00Z'};
      axios.post(`http://127.0.0.1:8000/backend_app/task`, request)
          .then(response => {
            if (response.status === 201) {
              this.$data.subpage = 'Tasks';
              console.log(response.status);
              window.location.reload();
            }
          })
          .catch(error => {
            console.log(error);
          })
    }
  },
  created() {
    this.$data.profile_type = localStorage.profile_type;
    axios.get(`http://127.0.0.1:8000/backend_app/task?query=byuserid&id=${localStorage.userid}`)
        .then(response => {
          if (response.status === 200) {
            let i;
            for (i = 0; i < response.data.length; i++) {
              console.log(response.data[i]['completion_time']);
              if (response.data[i]['completion_time'] === null) {
                this.$data.assigned_tasks.push(response.data[i]);
              }
              else {
                this.$data.completed_tasks.push(response.data[i]);
              }
            }
            console.log(this.$data.assigned_tasks);
          }
        })
        .catch(error => {
          console.log(error);
        });
    axios.get(`http://127.0.0.1:8000/backend_app/pairs?tutorid=${localStorage.userid}`)
        .then(response => {
          if (response.status === 200) {
            let i;
            for (i = 0; i < response.data.length; i++) {
              axios.get(`http://127.0.0.1:8000/backend_app/user?query=id&id=${response.data[i].student_id}`)
                  .then(response => {
                    if (response.status === 200) {
                      // this.$data.students.ids.push(response.data[0].id);
                      // this.$data.students.names.push(response.data[0].name);
                      this.$data.students.push(response.data[0]);
                    }
                  })
                  .catch(error => {
                    console.log(error);
                  })
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
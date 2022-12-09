<template>
  <v-app id="main">
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

        <v-avatar
            class="mr-10"
            color="grey darken-1"
            size="32"
        >
          <v-icon>mdi-account-circle</v-icon>
        </v-avatar>
        <v-btn
          icon
        >
          <router-link to="/login">
            <v-icon> mdi-logout </v-icon>
          </router-link>
        </v-btn>
      </v-container>
    </v-app-bar>
    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet class="rounded-lg">
              <v-list color="transparent">
                <v-list-item
                    v-for="link in links"
                    :key="link"
                    link
                    @click="page=link; subpage='none'"
                >
                  <v-list-item-content>
                    <v-list-item-title>
                      {{ link }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col cols="2" v-if="page==='Сообщения'">
            <v-sheet
                class="overflow-y-auto rounded-l-lg"
                min-height="80vh"
                max-height="80vh"
            >
                <v-list
                    class="rounded-l-lg"
                    v-for="dialog in dialogs"
                    :key="dialog"
                >
                  <v-list-item
                      link
                      class="v-list-item--two-line"
                      @click="subpage=dialog"
                  >
                    <v-avatar color="grey darken-1" size="32">
                      <v-icon>{{dialog[0]}}</v-icon>
                    </v-avatar>
                    <v-list-item-content class="ml-3">
                      <v-list-item-title>
                        {{ dialog }}
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
          <v-col cols="10" v-if="page==='Задания'">
            <TasksTab/>
<!--            <v-sheet-->
<!--                class="overflow-y-auto rounded-l-lg"-->
<!--                min-height="80vh"-->
<!--                max-height="80vh"-->
<!--            >-->
<!--              <v-list-->
<!--                  class="rounded-l-lg"-->
<!--                  v-for="n in 15"-->
<!--                  :key="n"-->
<!--              >-->
<!--                <v-list-item-->
<!--                    link-->
<!--                    class="v-list-item&#45;&#45;two-line"-->
<!--                >-->
<!--                  <v-list-item-content>-->
<!--                    <v-list-item-title>-->
<!--                      Задание №{{ n }}-->
<!--                    </v-list-item-title>-->
<!--                    <v-list-item-subtitle>-->
<!--                      Some Text...-->
<!--                    </v-list-item-subtitle>-->
<!--                  </v-list-item-content>-->
<!--                </v-list-item>-->
<!--                <v-divider class="text-grey-lighten-1"></v-divider>-->
<!--              </v-list>-->
<!--              &lt;!&ndash;  &ndash;&gt;-->
<!--            </v-sheet>-->
          </v-col>
          <v-col cols="8" v-if="page==='Преподаватели'">
            <TutorsTab/>
          </v-col>
          <v-col cols="10" v-if="page==='Расписание'">
            <CalendarWidget/>
          </v-col>
          <v-col cols="8" v-if="page==='Сообщения'">
            <v-sheet
                min-height="80vh"
                max-height="80vh"
                class="rounded-r-lg overflow-y-auto"
            >
              <v-divider style="position: relative; top: 73vh" v-if="subpage!=='none'"></v-divider>
              <v-container style="position: relative; padding-top: 73.5vh" v-if="subpage!=='none'">
                <v-responsive width="90vh" style="position: absolute; left: 5px">
                  <v-text-field
                      dense
                      flat
                      hide-details
                      solo-inverted
                      class="rounded-lg"
                  ></v-text-field>
                </v-responsive>
                <v-icon large style="position: absolute; right: 10px">mdi-send</v-icon>
              </v-container>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import CalendarWidget from "@/components/CalendarWidget";
import TasksTab from "@/components/TasksTab";
import TutorsTab from "@/components/TutorsTab";

export default {
  name: 'MainTab',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    CalendarWidget,
    TasksTab,
    TutorsTab
  },
  data: () => ({
    page:'messages',
    subpage: 'none',
    dialogs: [
      'Раиса',
      'Марина',
      'Анатолий',
      'Даниил',
      'Степан',
      'Егор',
      'Полина',
      'Варвара',
      'Дмитрий',
      'Надежда',
      'Александра',
      'Виктория',
      'Евгений',
      'Кристина',
      'Амина',
      'Руслан',
      'Марк'
    ],
    links: [
      'Сообщения',
      'Задания',
      'Преподаватели',
      'Тесты',
      'Расписание'
    ],
    items: [
      'Messages',
      'Teachers',
      'Tasks'
    ],
    tasks: [
      'Математика',
      'Физика',
      'Информатика',
      'Английский Язык'
    ]
  }),
}
</script>
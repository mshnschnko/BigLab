<template>
  <v-app id="inspire">
    <v-app-bar
        app
        color="white"
        flat
    >
      <v-container class="fill-height">
<!--        <v-avatar-->
<!--          class="mr-10"-->
<!--          color="grey darken-1"-->
<!--        >-->
<!--          <v-icon icon="mdi-account-circle"></v-icon>-->
<!--        </v-avatar>-->

<!--        <v-btn-->
<!--            v-for="link in links"-->
<!--            :key="link"-->
<!--            text-->
<!--        >-->
<!--          {{ link }}-->
<!--        </v-btn>-->
        <v-responsive max-width="270px" max-height="30px" class="rounded-lg">
          <v-textarea class="mt-0">
            <v-input class="align-center position-relative"></v-input>
          </v-textarea>
        </v-responsive>
<!--        <v-spacer class="px-12"></v-spacer>-->
        <v-btn link class="float-md-right rounded-circle align-start">
          <v-avatar
              color="grey darken-1"
          >
            <v-icon icon="mdi-account-circle"></v-icon>
          </v-avatar>
        </v-btn>
<!--        <v-btn class="float-md-right">-->
<!--          Выход-->
<!--        </v-btn>-->

<!--        <v-responsive max-width="150" class="v-responsive__content rounded-lg">-->
<!--          <v-text-field>-->
<!--            <div class="v-input v-input&#45;&#45;hide-details v-input&#45;&#45;dense theme&#45;&#45;light v-text-field v-text-field&#45;&#45;single-line v-text-field&#45;&#45;solo v-text-field&#45;&#45;solo-inverted v-text-field&#45;&#45;solo-flat v-text-field&#45;&#45;is-booted v-text-field&#45;&#45;enclosed v-text-field&#45;&#45;rounded"></div>-->
<!--          </v-text-field>-->
<!--        </v-responsive>-->

<!--        <v-responsive max-width="260">-->
<!--          <v-text-field-->
<!--              class="mr-10"-->
<!--          >-->
<!--            <v-input class="v-input__slot">-->
<!--            </v-input>-->
<!--          </v-text-field>-->
<!--        </v-responsive>-->
      </v-container>
    </v-app-bar>

    <v-main class="bg-grey-lighten-2">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet class="rounded-lg">
              <v-list class="rounded-lg">
                <v-list-item
                    v-for="link in links"
                    :key="link"
                    link
                    @click="page=link"
                >
                  <v-list-item-media>
                    <v-list-item-title>
                      {{ link }}
                    </v-list-item-title>
                  </v-list-item-media>
                </v-list-item>

<!--                <v-divider class="text-grey-lighten-1"></v-divider>-->

<!--                <v-list-item-->
<!--                    link-->
<!--                >-->
<!--                  <v-list-item-title>-->
<!--                    Refresh-->
<!--                  </v-list-item-title>-->
<!--                </v-list-item>-->
              </v-list>
            </v-sheet>
          </v-col>

          <v-col cols="3" v-if="page==='Сообщения'">
            <v-sheet
                min-height="80vh"
                max-height="80vh"
                class="rounded-s-lg overflow-y-auto flex-wrap"
            >
              <v-list
                  v-for="n in 15"
                  :key="n"
              >
                <v-list-item link class="v-list-item--two-line">
<!--                  <v-container>-->
                    <v-avatar color="grey darken-1" size="32">
                      <v-icon icon="mdi-account-circle"></v-icon>
                    </v-avatar>
                    <v-list-item-title>Собеседник №{{ n }}</v-list-item-title>
                    <v-list-item-subtitle>Some text</v-list-item-subtitle>
<!--                  </v-container>-->
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col cols="3" v-if="page==='Задания'">
            <v-sheet
                min-height="80vh"
                max-height="80vh"
                class="rounded-s-lg overflow-y-auto flex-wrap"
            >
              <v-list
                  v-for="n in 15"
                  :key="n"
              >
                <v-list-item link class="v-list-item--two-line">
                  <!--                  <v-container>-->
<!--                  <v-avatar color="grey darken-1" size="32">-->
<!--                    <v-icon icon="mdi-account-circle"></v-icon>-->
<!--                  </v-avatar>-->
                  <v-list-item-title>Заданиe №{{ n }}</v-list-item-title>
                  <v-list-item-subtitle>Some text</v-list-item-subtitle>
                  <!--                  </v-container>-->
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col cols="10" v-if="page==='Преподаватели'">
            <v-sheet
                min-height="80vh"
                max-height="80vh"
                class="rounded-s-lg overflow-y-auto flex-wrap"
            >
              <v-list
                  v-for="n in 15"
                  :key="n"
              >
                <v-list-item link class="v-list-item--two-line justify-sm-center">
                  <!--                  <v-container>-->
                  <v-avatar color="grey darken-1" size="32">
                    <v-icon icon="mdi-account-circle"></v-icon>
                  </v-avatar>
                  <v-list-item-title>Преподаватель №{{ n }}</v-list-item-title>
                  <v-list-item-subtitle>Some text</v-list-item-subtitle>
                  <!--                  </v-container>-->
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>

<!--              <v-col cols="2" class="border-e-sm flex-wrap" min_width="300px">-->
<!--               <v-sheet color="red" min-width="25vh" class="flex-wrap overflow-y-auto">-->
<!--                 <v-list-->
<!--                     style="display: flex"-->
<!--                     v-for="n in 15"-->
<!--                     :key="n"-->
<!--                 >-->
<!--                     <v-list-item link class="v-list-item&#45;&#45;two-line">-->
<!--    &lt;!&ndash;                     <v-avatar color="grey darken-1" size="32">&ndash;&gt;-->
<!--    &lt;!&ndash;                       <v-icon icon="mdi-account-circle"></v-icon>&ndash;&gt;-->
<!--    &lt;!&ndash;                     </v-avatar>&ndash;&gt;-->
<!--                       <v-list-item-title>-->
<!--                         Задание №{{ n }}-->
<!--                       </v-list-item-title>-->
<!--                       <v-list-item-subtitle>Some text</v-list-item-subtitle>-->
<!--                     </v-list-item>-->
<!--    &lt;!&ndash;                 </v-container>&ndash;&gt;-->
<!--                     <v-divider class="text-grey-lighten-1"></v-divider>-->
<!--                 </v-list>-->
<!--               </v-sheet>-->
<!--             </v-col>-->


          <v-col cols="7" v-if="page!=='Преподаватели' && page!=='Расписание'">
              <v-sheet
              min-height="80vh"
              max-height="80vh"
              class="rounded-e-lg"
              >

              </v-sheet>
          </v-col>

          <v-col cols="7" v-if="page==='Расписание'">
            <CalendarWidget></CalendarWidget>
          </v-col>

        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import CalendarWidget from "@/components/CalendarWidget";

export default {
  name: 'MainTab',
  components: {CalendarWidget},
  data: () => ({
    page:'messages',
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

<style>
.v-main__wrap {
  flex: 1 1 auto;
  max-width: 100%;
  position: relative;
}

.dialog-preview {
  min-width: 150px;
  width: 100%;
}
</style>
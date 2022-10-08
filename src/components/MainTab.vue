<template>
  <v-app id="inspire">
    <v-app-bar
        app
        color="white"
        flat
        class="mx-auto"
    >
      <v-container class="fill-height">
        <v-avatar
          class="mr-10"
          color="grey darken-1"
        >
<!--            class="mr-10"-->
<!--            color="grey darken-1"-->
<!--            size="32"-->
<!--        >-->
          <v-icon icon="mdi-account-circle"></v-icon>
        </v-avatar>

        <v-btn
            v-for="link in links"
            :key="link"
            text
        >
          {{ link }}
        </v-btn>
<!--        <v-spacer class="px-12"></v-spacer>-->
        <v-btn class="float-md-right">
          Выход
        </v-btn>

<!--        <v-responsive max-width="260">-->
<!--          <v-text-field-->
<!--              class="v-input&#45;&#45;horizontal v-input&#45;&#45;density-compact v-text-field rounded-lg"-->
<!--          >-->
<!--            <v-input class="v-input__control">-->
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
                    v-for="task in tasks"
                    :key="task"
                    link
                >
                  <v-list-item-media>
                    <v-list-item-title>
                      {{ task }}
                    </v-list-item-title>
                  </v-list-item-media>
                </v-list-item>

<!--                <v-divider class="text-grey-lighten-1"></v-divider>-->

<!--                <v-list-item-->
<!--                    link-->
<!--                >-->
<!--                  <v-list-item-media>-->
<!--                    <v-list-item-title>-->
<!--                      Refresh-->
<!--                    </v-list-item-title>-->
<!--                  </v-list-item-media>-->
<!--                </v-list-item>-->
              </v-list>
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet
                min-height="70vh"
                max-height="70vh"
                rounded="lg"
            >
             <v-col cols="2" class="border-e-sm" width="150px">
               <v-list
                 v-for="n in 15"
                 :key="n"
               >
<!--                 <v-container class="">-->
                 <v-list-item link class="v-list-item--two-line">
<!--                     <v-avatar color="grey darken-1" size="32">-->
<!--                       <v-icon icon="mdi-account-circle"></v-icon>-->
<!--                     </v-avatar>-->
                   <v-list-item-media>
                     <v-list-item-title>
                       Задание №{{ n }}
                     </v-list-item-title>
                     <v-list-item-subtitle>Some text</v-list-item-subtitle>
                   </v-list-item-media>
                 </v-list-item>
<!--                 </v-container>-->
                 <v-divider class="text-grey-lighten-1"></v-divider>
               </v-list>
             </v-col>
              <v-col>

              </v-col>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    links: [
      'Сообщения',
      'Задания',
      'Преподаватели',
      'Тесты',
      'Профиль'
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
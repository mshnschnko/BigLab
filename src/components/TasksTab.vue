<template>
  <v-app id="inspire">
    <v-app-bar
        app
        color="white"
        flat
    >
      <v-container class="py-0 fill-height">
        <v-responsive max-width="260">
          <v-text-field
              dense
              flat
              hide-details
              rounded
              solo-inverted
              placeholder="Поиск"
          ></v-text-field>
        </v-responsive>

        <v-spacer></v-spacer>

        <v-btn class="ma-2"
               text
        >Профиль
        </v-btn>

        <v-avatar
            class="mr-10"
            color="grey darken-1"
            size="32"
        >
          <v-icon icon="mdi-account-circle"></v-icon>
        </v-avatar>

      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
              <v-list color="transparent">
                <!--                <v-list-item-->
                <!--                    v-for="section in sections"-->
                <!--                    :key="section"-->
                <!--                    link-->
                <!--                >-->
                <!--                  <v-list-item-content>-->
                <!--                    <v-list-item-title>-->
                <!--                      {{ section }}-->
                <!--                    </v-list-item-title>-->
                <!--                  </v-list-item-content>-->
                <!--                </v-list-item>-->

                <v-list-item-group v-model="model">
                  <v-list-item
                      v-for="(item, i) in items"
                      :key="i"
                  >
                    <v-list-item-icon>
                      <v-icon v-text="item.icon"></v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title v-text="item.text"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>

                <v-divider class="my-2"></v-divider>

                <v-list-item
                    link
                    color="grey lighten-4"
                >
                  <v-list-item-content>
                    <v-list-item-title>
                      Refresh
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col>
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
                <!--                <v-menu transition="slide-y-transition">-->
                <!--                  <template v-slot:activator="{ on, attrs }">-->
                <!--                    <v-btn-->
                <!--                        text-->
                <!--                        color="grey"-->
                <!--                        class="mt-3"-->
                <!--                        v-bind="attrs"-->
                <!--                        v-on="on"-->
                <!--                    >-->
                <!--                      Репетиторы-->
                <!--                    </v-btn>-->
                <!--                  </template>-->
                <v-col cols="3">
                  <v-select
                      clearable
                      :items="teachers"
                      label="Репетиторы"
                  ></v-select>
                    <!--                </v-menu>-->
                </v-col>
              </v-tabs>
            </v-toolbar>

            <v-divider></v-divider>

            <v-sheet
                min-height="70vh"
                class="rounded-lg rounded-t-0"
            >
              <v-col
                  v-for="card in cards"
                  :key="card"
                  cols="12"
              >
                <v-card>
                  <v-subheader>{{ card }}</v-subheader>

                  <v-list two-line>
                    <template v-for="n in 6">
                      <v-list-item

                          :key="n"
                      >
                        <v-list-item-avatar color="grey darken-1">
                        </v-list-item-avatar>

                        <v-list-item-content>
                          <v-list-item-title>Задание {{ n }}</v-list-item-title>

                          <v-list-item-subtitle>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique
                          </v-list-item-subtitle>
                        </v-list-item-content>
                      </v-list-item>

                      <v-divider
                          v-if="n !== 6"
                          :key="`divider-${n}`"
                          inset
                      ></v-divider>
                    </template>
                  </v-list>
                </v-card>
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
    tasks: [
        'Математика',
        'Физика',
    ],
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
}
</script>

<style scoped>

</style>
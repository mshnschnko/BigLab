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
          <v-col cols="3">
            <v-select
                clearable
                :items="teachers"
                label="Репетиторы"
            ></v-select>
          </v-col>
        </v-tabs>
      </v-toolbar>

      <v-divider></v-divider>

      <v-sheet
          min-height="70vh"
          max-height="70vh"
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
              <template v-for="n in 6">
                <v-list-item

                    :key="n"
                >
                  <v-list-item-avatar color="grey darken-1">
                  </v-list-item-avatar>

                  <v-list-item-content>
                    <v-list-item-title>Задание {{ n }}</v-list-item-title>

                    <v-list-item-subtitle>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio
                      similique
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
    </v-sheet>
  </div>
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
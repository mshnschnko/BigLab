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
export default {
  name: "TutorsTab",
  data: () => ({
    tutors: [
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
  })
}

</script>

<style scoped>

</style>
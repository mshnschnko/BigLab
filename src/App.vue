<template>
  <v-app>
    <v-main>
      <MainTab/>
    </v-main>
  </v-app>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import MainTab from "@/components/MainTab";

export default {
  name: 'App',

  components: {
    // eslint-disable-next-line vue/no-unused-components
    MainTab
  },

  data: () => ({
    //
  }),
}
</script>

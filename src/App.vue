<template>
  <v-app>
    <v-main>
      <MainTab/>
    </v-main>
  </v-app>
</template>

<script>
import MainTab from './components/MainTab';

export default {
  name: 'App',

  components: {
    MainTab
  },

  data: () => ({
    //
  }),
};
</script>

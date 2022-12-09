<template>
  <v-app>
    <v-main>
      <LogRegForm v-if="Page === 'log'"/>
      <MainTab v-if="Page === 'main'"/>
    </v-main>
  </v-app>
</template>

<script>
// import RegisterForm from './components/RegisterForm';
// import LoginForm from "@/components/LoginForm";
import LogRegForm from "@/components/LogRegForm";
// import TutorsTab from "@/components/TutorsTab";
import MainTab from "@/components/MainTab";

export default {
  name: 'App',

  components: {
    LogRegForm,
    // TutorsTab,
    MainTab,
  },

  data: () => ({
    Page: 'main',
  }),
};
</script>

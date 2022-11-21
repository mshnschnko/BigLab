<template>
  <v-app>
    <v-main>
      <LogRegForm/>
    </v-main>
  </v-app>
</template>

<script>
// import RegisterForm from './components/RegisterForm';
// import LoginForm from "@/components/LoginForm";
import LogRegForm from "@/components/LogRegForm";

export default {
  name: 'App',

  components: {
    LogRegForm
  },

  data: () => ({
    //
  }),
};
</script>

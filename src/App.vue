<template>
  <v-app>
    <v-main>
      <RegisterForm/>
      <LoginForm/>
    </v-main>
  </v-app>
</template>

<script>
import RegisterForm from './components/RegisterForm';
import LoginForm from "@/components/LoginForm";

export default {
  name: 'App',

  components: {
    RegisterForm,
    LoginForm,
  },

  data: () => ({
    //
  }),
};
</script>

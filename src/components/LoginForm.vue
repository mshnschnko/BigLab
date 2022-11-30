<template>
  <v-container
    class="align-content-center"
  >
  <v-form
      class="align-content-center"
      v-if="LoginShow"
      ref="form"
      v-model="valid"
      lazy-validation
  >
    <v-text-field
        type="email"
        v-model="email"
        :rules="emailRules"
        label="E-mail"
        required
    ></v-text-field>

    <v-text-field
        type="password"
        v-model="password"
        :rules="passwordRules"
        label="Password"
        required
    ></v-text-field>

    <v-btn
        :disabled="!valid"
        color="success"
        class="rounded-lg mr-4"
        @click="validate"
    >
      Sign in
    </v-btn>

    <v-btn
        color="error"
        class="rounded-lg mr-4"
        @click="reset"
    >
      Reset Form
    </v-btn>
  </v-form>
    <v-banner v-if="SignedUpShow">You are signed in</v-banner>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  name: 'LoginForm',
  data: () => ({
    LoginShow: true,
    SignedUpShow: false,
    valid: true,
    name: '',
    nameRules: [
      v => !!v || 'Name is required',
      v => (v && v.length <= 30) || 'Name must be less than 30 characters',
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      // v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
    password: '',
    passwordRules: [
      v => !!v || 'Password is required',
      // v => /^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d).*$/.test(v) || 'Password must contain 8 characters and at least one number and one letter'
    ],
    select: null,
    items: [
      'Админ',
      'Ученик',
      'Репетитор',
    ],
    checkbox: false,
  }),
  methods: {
    validate () {
      this.$refs.form.validate();
      const request = {};
      axios.get(`http://127.0.0.1:8000/backend_app/getuser/?email=${this.$data.email}`, request)
          .then(response => {
            console.log(response.data);
            this.$data.ShowValue = false;
            this.$data.SignedUpShow = true;
          })
          .catch(error => console.log(error));
    },
    reset () {
      this.$refs.form.reset()
    },
    resetValidation () {
      this.$refs.form.resetValidation()
    },
  },
}
</script>

<style scoped>

</style>
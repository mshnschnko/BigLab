<template>
  <v-form
      v-if="RegisterShow"
      ref="form"
      v-model="valid"
      lazy-validation
  >
    <v-text-field
        v-model="name"
        :counter="30"
        :rules="nameRules"
        label="Name"
        required
    ></v-text-field>

    <v-text-field
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

    <v-select
        v-model="select"
        :items="items"
        :rules="[v => !!v || 'Item is required']"
        label="Item"
        required
    ></v-select>

    <v-checkbox
        v-model="checkbox"
        :rules="[v => !!v || 'You must agree to continue!']"
        label="Do you agree?"
        required
    ></v-checkbox>

    <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        @click="validate"
    >
      Sign Up
    </v-btn>

    <v-btn
        color="error"
        class="mr-4"
        @click="reset"
    >
      Reset Form
    </v-btn>

  </v-form>
</template>

<script>
import axios from 'axios';
export default {
  name: 'RegisterForm',
  data: () => ({
    RegisterShow: true,
    valid: true,
    name: '',
    nameRules: [
      v => !!v || 'Name is required',
      v => (v && v.length <= 30) || 'Name must be less than 30 characters',
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
    password: '',
    passwordRules: [
        v => !!v || 'Password is required',
        v => /^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d).*$/.test(v) || 'Password must contain 8 characters and at least one number and one letter'
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
      let role = "0";
      switch (this.$data.select) {
        case "Админ":
          role = "1";
          break;
        case "Ученик":
          role = "2";
          break;
        case "Репетитор":
          role = "3";
          break;
      }
      const request = {username: this.$data.email.slice(0, this.$data.email.indexOf("@")),
                      name: this.$data.name,
                      email: this.$data.email,
                      raw_password: this.$data.password,
                      password: this.$data.password,
                      profile_type: role};
      axios.post("http://127.0.0.1:8000/backend_app/register/", request)
          .then(response => console.log(response.status))
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
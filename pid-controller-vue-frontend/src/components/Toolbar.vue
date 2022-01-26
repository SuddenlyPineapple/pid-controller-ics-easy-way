<template>
  <v-app-bar app color="primary">
    <v-app-bar-nav-icon
      class="hidden-md-and-up white--text"
      @click="toggleDrawer"
    />
    <v-toolbar-title class="headline text-uppercase">
      <span class="accent--text">Inteligent</span>
      <span class="font-weight-light white--text">Control</span>
      <span class="accent--text">Systems</span>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn
        v-for="(route, i) in routes"
        :key="i"
        :to="route.to"
        class="ml-0 hidden-sm-and-down white--text"
        text
      >
        {{ route.text }}
      </v-btn>
    </v-toolbar-items>
  </v-app-bar>
</template>

<script>
import { mapMutations } from "vuex";
export default {
  computed: {
    routes() {
      return this.$store.state.routes;
    },
  },
  methods: {
    ...mapMutations(["toggleDrawer"]),
  },
};
</script>

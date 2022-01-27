<template>
  <v-navigation-drawer v-model="drawer" app temporary color="primary">
    <v-container>
      <v-flex xs12 class="text-xs-center my-4">
        <h1 class="headline text-uppercase">
          <span class="accent--text">Inteligent</span><br />
          <span class="font-weight-light white--text">Control</span><br />
          <span class="accent--text">Systems</span>
        </h1>
      </v-flex>
    </v-container>

    <v-divider></v-divider>
    <v-list>
      <v-list-item
        v-for="(route, i) in routes"
        :key="i"
        :to="route.to"
        :href="route.to"
        text
        @click="onClick($event, route)"
      >
        <v-list-item-action>
          <v-icon>{{ route.icon }}</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title v-text="route.text" class="white--text" />
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapMutations } from "vuex";
export default {
  name: "Drawer",
  computed: {
    routes() {
      return this.$store.state.routes;
    },
    drawer: {
      get() {
        return this.$store.state.drawer;
      },
      set(val) {
        this.setDrawer(val);
      },
    },
  },
  methods: {
    ...mapMutations(["setDrawer"]),
    onClick(e, item) {
      e.stopPropagation();
      if (item.to === "/") {
        this.$vuetify.goTo(0);
        this.setDrawer(false);
        return;
      }
      if (item.to || !item.href) {
        return;
      }
      this.$vuetify.goTo(item.href);
      this.setDrawer(false);
    },
  },
};
</script>

<style lang="scss">
.absolute-logo {
  position: absolute;
  bottom: 5%;
  left: 20px;
}
.v-list__tile--active {
  color: orange !important;
  caret-color: orange !important;
}
.center {
  text-align: center;
}
</style>

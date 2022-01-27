import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    drawer: false,
    routes: [
      {
        text: "Simulation",
        to: "/simulation",
      },
      {
        text: "Set Parameters",
        to: "/",
      },
      {
        text: "About",
        to: "/about",
      },
    ],
  },
  getters: {
    routes: (state) => state.routes,
  },
  mutations: {
    setDrawer: (state, payload) => (state.drawer = payload),
    toggleDrawer: (state) => (state.drawer = !state.drawer),
  },
  actions: {},
});

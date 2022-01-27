<template>
  <v-footer color="primary">
    <v-card flat tile class="primary white--text text-center">
      <v-card-text>
        <v-btn
          v-for="link in socialMedia"
          :key="link.icon"
          class="mx-4 white--text"
          icon
          :href="link.link"
        >
          <v-icon size="24px" color="accent">{{ link.icon }}</v-icon>
        </v-btn>
      </v-card-text>

      <v-row>
        <v-col cols="12" md="9" class="px-5">
          <v-card-text class="white--text pt-0 text-left">
            PID and Fuzzy PID regulator logic simulation project for Intelligent
            Control Systems classes at Poznan University of Technology.
          </v-card-text>
          <v-card-text class="white--text pt-0 text-left">
            Made with 💖 using
            <strong class="accent--text">Python</strong>,
            <strong class="accent--text">Flask</strong> with a bit of
            concurrency, <strong class="accent--text">Vue</strong> and
            <strong class="accent--text">Vuetify.</strong>
          </v-card-text>
        </v-col>
        <v-col cols="12" md="3" class="max-height pt-0">
          <v-img
            :src="ppLogo"
            alt="Politechnika Poznańska Logo"
            height="80"
            contain
          />
        </v-col>
      </v-row>

      <v-divider />

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} —
        <strong>
          &copy;
          <a
            href="mailto:wojciech.kasperski97@gmail.com"
            class="font-weight-light white--text"
          >
            Wojciech Kasperski
          </a>
        </strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: "Footer",
  data: () => ({
    socialMedia: [
      {
        icon: "mdi-github",
        link: "https://github.com/SuddenlyPineapple",
      },
      {
        icon: "mdi-vuejs",
        link: "https://vuejs.org/",
      },
      {
        icon: "mdi-vuetify",
        link: "https://vuetifyjs.com/en/",
      },
    ],
    ppLogo: require("../assets/PolitechnikaPoznanska.png"),
  }),
};
</script>

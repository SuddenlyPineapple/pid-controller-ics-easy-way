<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12">
          <h1>Set parameters</h1>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>Sampling time (s)</h3>
          <v-slider
            v-model="parameters.sample_time"
            class="align-center mb-0 pb-0"
            :max="2"
            :min="0"
            :step="0.05"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.sample_time"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>Differential Time (s)</h3>
          <v-slider
            v-model="parameters.differential_time"
            class="align-center mb-0 pb-0"
            :max="1"
            :min="0"
            :step="0.01"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.differential_time"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>Integration Time (s)</h3>
          <v-slider
            v-model="parameters.integration_time"
            class="align-center mb-0 pb-0"
            :max="2"
            :min="0"
            :step="0.05"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.integration_time"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>Gain</h3>
          <v-slider
            v-model="parameters.gain"
            class="align-center mb-0 pb-0"
            :max="10"
            :min="0"
            :step="0.1"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.gain"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>Error (k_e)</h3>
          <v-slider
            v-model="parameters.k_e"
            class="align-center mb-0 pb-0"
            :max="10"
            :min="-10"
            :step="0.05"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.k_e"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>Current Error (k_ce)</h3>
          <v-slider
            v-model="parameters.k_ce"
            class="align-center mb-0 pb-0"
            :max="10"
            :min="-10"
            :step="0.05"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.k_ce"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>Initial error (k_u)</h3>
          <v-slider
            v-model="parameters.k_u"
            class="align-center mb-0 pb-0"
            :max="parameters.u_max"
            :min="parameters.u_min"
            :step="0.01"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.k_u"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>Maximum height of the reservoir</h3>
          <v-slider
            v-model="parameters.h_max"
            class="align-center mb-0 pb-0"
            :max="100"
            :min="0"
            :step="0.1"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.h_max"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>The value of the task (h_z in meters)</h3>
          <v-slider
            v-model="parameters.h_z"
            class="align-center mb-0 pb-0"
            :max="parameters.h_max"
            :min="0"
            :step="0.1"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.h_z"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>The cross-sectional area of the reservoir (A[m2])</h3>
          <v-slider
            v-model="parameters.A"
            class="align-center mb-0 pb-0"
            :max="100"
            :min="0"
            :step="0.25"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.A"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>Discharge factor (B)</h3>
          <v-slider
            v-model="parameters.B"
            class="align-center mb-0 pb-0"
            :max="10"
            :min="0"
            :step="0.01"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.B"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>The maximum value of the offset (u_max)</h3>
          <v-slider
            v-model="parameters.u_max"
            class="align-center mb-0 pb-0"
            :max="10"
            :min="0"
            :step="0.01"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.u_max"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>The minimum value of the offset (u_min)(</h3>
          <v-slider
            v-model="parameters.u_min"
            class="align-center mb-0 pb-0"
            :max="10"
            :min="0"
            :step="0.01"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.u_min"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>Maximum inflow rate (Q_d_max)</h3>
          <v-slider
            v-model="parameters.Q_d_max"
            class="align-center mb-0 pb-0"
            :max="10"
            :min="0"
            :step="0.01"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.Q_d_max"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
        <v-col cols="12" md="6" lg="4" xl="3">
          <h3>Minimum inflow rate (Q_d_min)</h3>
          <v-slider
            v-model="parameters.Q_d_min"
            class="align-center mb-0 pb-0"
            :max="10"
            :min="0"
            :step="0.01"
          >
            <template v-slot:append>
              <v-text-field
                v-model="parameters.Q_d_min"
                class="mt-0 pt-0 align-center"
                hide-details
                single-line
                type="number"
                style="width: 60px"
              />
            </template>
          </v-slider>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" class="text-center">
          <v-btn @click="saveParameteres" color="primary">
            Save Parameters
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
    <v-snackbar
      v-model="snackbar"
      :color="snackColor"
      :timeout="5000"
      multi-line
      bottom
      right
    >
      {{ message }}
    </v-snackbar>
  </div>
</template>

<script>
import axios from "axios";
import { apiUrl } from "../config";

export default {
  name: "SetParametersPage",
  data: () => ({
    parameters: {
      sample_time: 0.05,
      differential_time: 0.15,
      integration_time: 0.25,
      gain: 0.1,
      k_e: 0.2,
      k_ce: 0.05,
      k_u: 0.1,
      h_z: 8,
      A: 2.5,
      B: 0.25,
      h_max: 10,
      u_max: 10,
      u_min: -10,
      Q_d_max: 1,
      Q_d_min: 0,
    },
    message: "",
    snackColor: "",
    snackbar: false,
  }),
  methods: {
    saveParameteres() {
      axios
        .post(
          apiUrl +
            "/set-params?" +
            "sample_time=" +
            this.parameters.sample_time +
            "&" +
            "differential_time=" +
            this.parameters.differential_time +
            "&" +
            "integration_time=" +
            this.parameters.integration_time +
            "&" +
            "gain=" +
            this.parameters.gain +
            "&" +
            "k_e=" +
            this.parameters.k_e +
            "&" +
            "k_ce=" +
            this.parameters.k_ce +
            "&" +
            "k_u=" +
            this.parameters.k_u +
            "&" +
            "h_z=" +
            this.parameters.h_z +
            "&" +
            "A=" +
            this.parameters.A +
            "&" +
            "B=" +
            this.parameters.B +
            "&" +
            "h_max=" +
            this.parameters.h_max +
            "&" +
            "u_max=" +
            this.parameters.u_max +
            "&" +
            "u_min=" +
            this.parameters.u_min +
            "&" +
            "Q_d_max=" +
            this.parameters.Q_d_max +
            "&" +
            "Q_d_min=" +
            this.parameters.Q_d_min +
            "&"
        )
        .then((response) => {
          // console.log(response);
          this.snackColor = "green";
          this.message = response.data.message;
          this.snackbar = true;
        })
        .catch((err) => {
          console.error(err);
          this.snackColor = "red";
          this.message = err.response.data.message;
          this.snackbar = true;
        });
    },
  },
};
</script>

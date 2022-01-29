<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12">
          <h1>Run some nice simulations here!</h1>
        </v-col>
        <v-col cols="12">
          <h2>
            API Concurrent job handler status:
            <span v-if="busy" class="grey--text">
              <v-icon class="red--text">mdi-spin mdi-loading</v-icon> BUSY
            </span>
            <span v-else class="grey--text">
              <v-icon class="green--text">mdi-check-circle-outline</v-icon>
              READY
            </span>
          </h2>
        </v-col>
        <v-col cols="12" md="3">
          <v-select
            v-model="selectedSimulation"
            :items="simulationTypes"
            label="Simulation type"
            item-text="state"
            item-value="value"
          />
        </v-col>
        <v-col cols="12" md="9" class="d-flex align-center">
          <v-btn
            @click="dispatchSimulation"
            color="primary"
            :disabled="!selectedSimulation || busy"
          >
            RUN SIMULATION
          </v-btn>
        </v-col>
        <v-col cols="12">
          <v-btn
            @click="getChart('/get-pid-chart')"
            color="primary"
            class="mr-4"
          >
            Get PID Chart
          </v-btn>
          <v-btn
            @click="getChart('/get-fuzzy-chart')"
            color="primary"
            class="mr-4"
          >
            Get Fuzzy PID Chart
          </v-btn>
          <v-btn @click="getChart('/get-pid-and-fuzzy-chart')" color="primary">
            Get PID & Fuzzy Comparsion Chart
          </v-btn>
        </v-col>
        <v-col cols="12" class="text-center">
          <v-img
            v-if="!!chartImage && !isLoading"
            :src="chartImage"
            height="500px"
            contain
          />
          <v-progress-circular
            v-else-if="isLoading"
            :size="70"
            :width="7"
            color="primary"
            indeterminate
          />
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
  name: "Simulation",
  data: () => ({
    busy: false,
    chartImage: null,
    isLoading: false,
    simulationTypes: [
      { state: "PID", value: "/generate-pid" },
      { state: "FUZZY", value: "/generate-fuzzy" },
      { state: "COMPARISON", value: "/generate-comparison" },
    ],
    selectedSimulation: null,
    snackbar: false,
    snackColor: "green",
    message: "",
  }),
  methods: {
    checkStatus() {
      //console.log("check status");
      axios
        .get(apiUrl + "/state")
        .then((response) => {
          if (response.status === 200) {
            this.busy = false;
            setTimeout(this.checkStatus, 10000);
          } else {
            this.busy = true;
            setTimeout(this.checkStatus, 5000);
          }
        })
        .catch(() => {
          this.busy = true;
          setTimeout(this.checkStatus, 5000);
        });
    },
    getChart(endpoint) {
      this.isLoading = true;
      axios
        .get(apiUrl + endpoint, { responseType: "arraybuffer" })
        .then((response) => {
          var bytes = new Uint8Array(response.data);
          var binary = bytes.reduce(
            (data, b) => (data += String.fromCharCode(b)),
            ""
          );
          this.chartImage = "data:image/jpeg;base64," + btoa(binary);
        })
        .catch((err) => {
          console.error(err);
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
    dispatchSimulation() {
      axios
        .post(apiUrl + this.selectedSimulation)
        .then((response) => {
          if (response.status === 201) {
            this.busy = true;
            this.snackColor = "green";
            this.message = response.data.message;
            this.snackbar = true;
          }
        })
        .catch((err) => {
          this.snackColor = "red";
          this.message = err.response.data.message;
          this.snackbar = true;
        });
    },
  },
  mounted() {
    this.checkStatus();
  },
};
</script>

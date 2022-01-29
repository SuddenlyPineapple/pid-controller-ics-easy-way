<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <div class="about">
          <h1>How to use this app?</h1>
          <ol>
            <li>
              set value of parameters in <strong>SET PARAMETERS</strong> tab and
              remeber to save them to API, by clicking
              <strong>SAVE PARAMETERS</strong> button
            </li>
            <li>
              then run simulation by choosing one mode
              <strong>PID, FUZZY, COMPARISON [PID and FUZZY]</strong> and click
              <strong>RUN SIMULATION</strong> button
            </li>
            <li>
              now wait till API job handler do your requested task and go into
              <strong>READY</strong> state
            </li>
            <li>
              then you can fetch results for desired simulation, by clicking
              appropriate to simulation mode button
            </li>
            <li>
              aplication can store up to 1 result for given modes and you can
              also fetch old results while waiting for new ones
            </li>
          </ol>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

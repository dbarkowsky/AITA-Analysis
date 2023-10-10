<script setup lang="ts"></script>

<template>
  <v-container fluid class="main-container">
    <v-row justify="center" align-content="center">
      <v-col lg="7" md="9" sm="12">
        <h1>r/AmITheAsshole</h1>
        <h3>A Data Survey</h3>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col lg="7" md="9" sm="12">
        <p>This is some text.</p>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col lg="7" md="9" sm="12">
        <img src="./assets/charts/AverageNumberofCommentsperFlair.svg" />
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped lang="scss">
@import "./colours.scss";
.main-container {
  background-color: $beige;
  color: $text-dark;
  width: 100vw;
  padding: 2em 0;
}
</style>

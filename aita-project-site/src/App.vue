<script setup lang="ts"></script>

<template>
  <v-container fluid class="main-container">
    <v-row justify="center" align-content="center">
      <v-col lg="7" md="9" sm="12">
        <h1>r/AmItheAsshole</h1>
        <h3>A Data Survey</h3>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col lg="5" md="7" sm="12">
        <p>
          My wife browses a lot of
          <a href="https://www.reddit.com/r/AmItheAsshole/">r/AmItheAsshole</a>.
          If you're not familiar with it, it's a forum on the website
          <a href="https://www.reddit.com/">Reddit</a> that revolves around one
          thing: <b>judgement</b>.
        </p>
        <p>
          Users will post their stories looking for the assessment of their
          Reddit peers. The best of these stories are often tales of insane
          family members, bitter significant others, or petty acts of revenge.
        </p>
        <p>
          In the end, users will vote with the first line of their comments
          using acronyms like YTA or NTA. After 18 hours, the verdict is in as
          the top-rated comment has their vote applied to the post as a flair.
        </p>
        <p>For example:</p>
        <img class="styled-image" src="./assets/images/sample_post.png" />
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col>
        <h3>The Original Hypothesis</h3>
        <p></p>
      </v-col>
      <v-col lg="7" md="8" sm="12" cols="12">
        <img src="./assets/charts/AverageNumberofCommentsperFlair.svg" />
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col>
        <h3>Collecting the Data</h3>
        <p></p>
      </v-col>
      <v-col lg="7" md="8" sm="12" cols="12"> </v-col>
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

.v-col {
  padding: 0.5em 2em;

  p {
    margin: 1em;
  }
}

.left-text {
  text-align: left;
}

.styled-image {
  border: 0.5em solid $red;
  border-radius: 1em;
  width: 100%;
}
</style>

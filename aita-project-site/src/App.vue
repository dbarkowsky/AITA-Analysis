<script setup lang="ts">
import Row from "./components/Row.vue";
import SingleRow from "./components/SingleRow.vue";
</script>

<template>
  <v-menu class="menu">
    <template v-slot:activator="{ props }">
      <v-btn color="primary" v-bind="props"> More</v-btn>
    </template>
    <v-list>
      <v-list-item>
        <v-list-item-title>GitHub</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
  <v-container fluid class="main-container">
    <v-row justify="center" align-content="center">
      <v-col lg="7" md="9" sm="12">
        <h1>r/AmItheAsshole</h1>
        <h3>A Data Survey</h3>
      </v-col>
    </v-row>
    <SingleRow v-slot:childSlot>
      <p>
        If you're not familiar with it,
        <a href="https://www.reddit.com/r/AmItheAsshole/">r/AmItheAsshole</a>
        is a forum on the website
        <a href="https://www.reddit.com/">Reddit</a> that revolves around one
        thing: <b>judgement</b>.
      </p>
      <p>
        Users will post their stories looking for the assessment of their Reddit
        peers. The best of these stories are often tales of insane family
        members, bitter significant others, or petty acts of revenge.
      </p>
      <p>
        In the end, users will vote with the first line of their comments using
        acronyms like YTA or NTA. After 18 hours, the verdict is in as the
        top-rated comment has their vote applied to the post as a flair.
      </p>
      <p class="left-text">For example:</p>
      <img class="styled-image" src="./assets/images/sample_post.png" />
    </SingleRow>
    <Row
      title="The Original Hypothesis"
      img="\src\assets\charts\scatterplot_LikelihoodofAssholeifRomanticandOlderbyAgeDifference.svg"
      v-slot:childSlot
    >
      <p>Let's cut right to the chase.</p>
      <p>
        My wife browses a lot of r/AmItheAsshole. Over time she felt like she
        noticed a particular trend:
        <b
          >posts where the original poster (OP) was writing about their romantic
          partner and where the OP was the older of the two</b
        >
        were more likely to be branded as assholes.
      </p>
      <p>
        The bigger the gap between the OP and the person they were writing
        about, the greater the chance that they would be viewed as assholes.
      </p>
      <p>
        This was the crux of the whole project, and as you can see from this
        chart, it wasn't a bad hypothesis. As the age gap between OP and partner
        widens, the asshole-ery starts to trend up.
      </p>
    </Row>
    <SingleRow v-slot:childSlot>
      <p>
        This does tend to get a little bit hazier as the age gap widens, just
        because there are way fewer data points to help calculate this gap.
      </p>
    </SingleRow>
  </v-container>
</template>

<style scoped lang="scss">
@import "./colours.scss";
.main-container {
  background-color: $beige;
  color: $text-dark;
  width: 100vw;
  padding: 2em 0 0 0;
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

@supports selector(:focus-visible) {
  .v-btn {
    position: fixed !important;
    top: 0.5em;
    left: 0.5em;
    background-color: $red !important;
    color: $text-dark !important;
  }
}
</style>

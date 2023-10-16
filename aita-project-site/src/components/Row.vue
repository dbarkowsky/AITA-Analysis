<script lang="ts">
import { defineProps } from "vue";

defineProps<{
  title: string;
  img: string;
  flip?: boolean;
  dark?: string;
}>();

export default {
  name: "Row",
  props: ["title", "flip", "dark", "img"],
};
</script>

<template>
  <v-row justify="center" :class="dark === 'true' ? 'dark' : ''">
    <v-col lg="2" cols="0"></v-col>
    <v-col>
      <h3>{{ title }}</h3>
      <slot name="childSlot"></slot>
    </v-col>
    <v-col lg="5" md="8" sm="12" cols="12">
      <img :src="img" />
    </v-col>
    <v-col lg="2" cols="0"></v-col>
  </v-row>
</template>

<style scoped lang="scss">
@import "../colours.scss";

.v-row.dark {
  background-color: $background-dark;
  color: $beige;
}
</style>

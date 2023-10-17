<script lang="ts">
import { defineProps } from "vue";

defineProps<{
  dark?: string;
  title?: string;
}>();

export default {
  name: "SingleRow",
  props: ["dark", "title"],
};
</script>

<template>
  <v-row v-if="title" :class="dark === 'true' ? 'dark' : ''">
    <v-col lg="6" md="6" sm="12">
      <h3 class="single-title">{{ title }}</h3>
    </v-col>
    <v-col> </v-col>
  </v-row>
  <v-row justify="center" :class="dark === 'true' ? 'dark' : ''">
    <v-col lg="7" md="8" sm="12">
      <slot name="childSlot"></slot>
    </v-col>
  </v-row>
</template>

<style scoped lang="scss">
@import "../colours.scss";

.v-row.dark {
  background-color: $background-dark;
  color: $beige;
}
</style>

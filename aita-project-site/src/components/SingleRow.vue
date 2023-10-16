<script lang="ts">
import { defineProps } from "vue";

defineProps<{
  dark?: string;
}>();

export default {
  name: "SingleRow",
  props: ["dark"],
};
</script>

<template>
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

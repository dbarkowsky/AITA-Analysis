<script lang="ts">
import { defineProps } from "vue";

defineProps<{
  dark?: string;
  img1?: string;
  img2?: string;
}>();

export default {
  name: "TwoChart",
  props: ["dark", "img1", "img2"],
};
</script>

<template>
  <v-row justify="center" :class="dark === 'true' ? 'dark' : ''">
    <v-col lg="1" md="0" cols="0"></v-col>
    <v-col lg="5" md="6" sm="12" cols="12">
      <img :src="img1" />
    </v-col>
    <v-col lg="5" md="6" sm="12" cols="12">
      <img :src="img2" />
    </v-col>
    <v-col lg="1" md="0" cols="0"></v-col>
  </v-row>
</template>

<style scoped lang="scss">
@import "../colours.scss";

.v-row.dark {
  background-color: $background-dark;
  color: $beige;
}
</style>

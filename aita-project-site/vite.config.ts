import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

const baseURL = !process.env.BASE_URL ? "/" : process.env.BASE_URL;

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: baseURL,
});

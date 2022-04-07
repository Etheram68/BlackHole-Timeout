import { createWebHistory, createRouter } from "vue-router";
import Home from "@/components/HomeView.vue";
import BlackHoleView from "@/components/BlackholeView.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/blackhole",
    name: "blackhole",
    component: BlackHoleView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

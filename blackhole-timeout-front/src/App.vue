<template>
  <div class="dark:bg-slate-800">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <header-top></header-top>
    <router-view></router-view>
    <footer-bottom></footer-bottom>
  </div>
</template>

<script>
  import HeaderTop from './components/Header'
  import FooterBottom from './components/Footer'

  export default {
    name: 'App',
    components: {
      'header-top': HeaderTop,
      'footer-bottom': FooterBottom
    }
  }
</script>

<style>
</style>

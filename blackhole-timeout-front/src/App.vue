<template>
  <div>
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <header-top></header-top>
    <router-view></router-view>
  </div>
</template>

<script>
  import HeaderTop from './components/Header'

  export default {
    name: 'App',
    components: {
      'header-top': HeaderTop,
    }
  }
</script>

<style>

</style>

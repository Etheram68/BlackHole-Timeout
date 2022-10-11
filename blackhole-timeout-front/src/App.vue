<template>
  <div class="dark:bg-gradient-to-b dark:from-slate-800 dark:to-slate-900">
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
	@media (prefers-color-scheme: dark) {
		body {
			background: #0f172a;
		}
	}
</style>

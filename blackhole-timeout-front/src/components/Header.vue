<template>
	<header class="sticky top-0 z-50">
		<nav class="relative flex flex-wrap items-center justify-between px-2 py-3 bg-cyan-500 mb-3">
			<div class="container px-4 mx-auto flex flex-wrap items-center justify-between">
				<div class="w-full relative flex justify-between lg:w-auto  px-4 lg:static lg:block lg:justify-start">
				<router-link class="text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase text-white" to="/">
					42 Blackhole Timeout
				</router-link>
				<button class="text-white cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none" type="button" v-on:click="toggleNavbar()">
					<svg class="h-6 w-6 fill-current" viewBox="0 0 24 24">
						<path v-if="isOpen" fill-rule="evenodd" d="M18.278 16.864a1 1 0 0 1-1.414 1.414l-4.829-4.828-4.828 4.828a1 1 0 0 1-1.414-1.414l4.828-4.829-4.828-4.828a1 1 0 0 1 1.414-1.414l4.829 4.828 4.828-4.828a1 1 0 1 1 1.414 1.414l-4.828 4.829 4.828 4.828z"/>
						<path v-if="!isOpen" fill-rule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"/>
					</svg>
				</button>
				</div>
				<div v-bind:class="{'hidden': !showMenu, 'flex': showMenu}" class="lg:flex lg:flex-grow items-center">
				<ul class="flex flex-col lg:flex-row list-none ml-auto">
					<li class="nav-item">
						<router-link class="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-white hover:opacity-75" to="/">
							<span class="ml-2">Home</span>
						</router-link>
					</li>
					<li class="nav-item">
						<router-link class="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-white hover:opacity-75" to="/blackhole">
							<span class="ml-2">Blackhole</span>
						</router-link>
					</li>
				</ul>
				</div>
			</div>
		</nav>
	</header>
</template>

<script>
	export default {
		name: 'HeaderTop',
		data() {
			return {
				showMenu: false,
				isOpen: false,
			}
		},
		methods: {
			toggleNavbar: function(){
				this.showMenu = !this.showMenu;
			}
		}
	}
</script>

<style scoped>

</style>

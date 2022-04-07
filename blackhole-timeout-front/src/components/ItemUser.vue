<template>
	<div class="md:flex">
		<div class="md:shrink-0">
			<img class="h-48 w-full object-cover md:h-full md:w-48" :src="urlImg=user.image_url" :alt="'profile_'+user.login">
		</div>
		<div class="p-8">
			<div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold" @click.prevent="openProfile(user.login)">{{ user.login }}</div>
			<p class="mt-2 text-slate-500">Email: {{ user.email }}</p>
			<p class="mt-2 text-slate-500">Days Left: {{ user.days_left }}</p>
			<p class="mt-2 text-slate-500">Last connexion: {{ convertDate(user.last_connection) }}</p>
		</div>
	</div>
</template>

<script>

	export default {
		props: ['user', 'convertDate'],
	}
</script>

<style scoped>
</style>

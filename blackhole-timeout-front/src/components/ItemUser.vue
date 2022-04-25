<template>
	<div class="sm:flex">
		<div class="sm:shrink-0">
			<img class="h-48 w-full object-cover sm:h-full sm:w-48" :src="urlImg=user.image_url" :alt="'profile_'+user.login">
		</div>
		<div class="p-8">
			<div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold" @click.prevent="openProfile(user.login)">{{ user.login }}</div>
			<p class="mt-2 text-slate-500">Email: {{ user.email }}</p>
			<p class="mt-2 text-slate-500">Days Left: {{ user.days_left }}</p>
			<p class="mt-2 text-slate-500" :title="title=convertDate(user.last_connection)">Last connexion: {{ deltaDays(user.last_connection) }} days</p>
		</div>
	</div>
</template>

<script>

	export default {
		props: ['user', 'convertDate', 'deltaDays'],
	}
</script>

<style scoped>
</style>

<template>
	<div class="sm:flex">
		<div class="sm:shrink-0">
			<img class="h-48 w-full object-cover sm:h-full sm:w-48" :src="urlImg=user.image_url" :alt="'profile_'+user.login">
		</div>
		<div class="p-8">
			<div id="login" class="uppercase tracking-wide text-sm text-indigo-500 font-semibold" @click.prevent="openProfile(user.login)" :title="title=concatUrl(user.login)">{{ user.login }}</div>
			<p class="mt-2 text-slate-500">Email: {{ user.email }}</p>
			<p class="mt-2 text-slate-500">Days Left: {{ user.days_left }}</p>
			<p class="mt-2 text-slate-500" :title="title=convertDate(user.last_connection)">Last connexion: {{ deltaDays(user.last_connection) }} days</p>
		</div>
	</div>
</template>

<script>

	export default {
		name: 'ItemUser',
		props: ['user', 'convertDate', 'deltaDays'],
		methods: {
			openProfile: function(login) {
				window.open('https://profile.intra.42.fr/users/'+login, '_blank');
			},
			concatUrl: function(login) {
				return 'https://profile.intra.42.fr/users/'+login
			}
		}
	}
</script>

<style scoped>
	#login {
		cursor: pointer;
	}
</style>

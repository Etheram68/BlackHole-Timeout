<template>
	<div class="sm:flex">
		<div class="sm:shrink-0">
			<img class="h-48 w-full object-cover sm:h-full sm:w-48" :src="urlImg=user.image_url" :alt="'profile_'+user.login">
		</div>
		<div class="p-8">
			<div id="login" class="uppercase tracking-wide text-sm text-indigo-500 font-semibold dark:text-indigo-400" @click.prevent="openProfile(user.login)" :data_title="data_title=concatUrl(user.login)">{{ user.login }}</div>
			<p class="mt-2 text-slate-500 dark:text-white">Email: {{ user.email }}</p>
			<p class="mt-2 text-slate-500 dark:text-white">Days Left: {{ user.days_left }}</p>
			<p class="mt-2 text-slate-500 dark:text-white" :data_title="data_title=convertDate(user.last_connection)">Last connexion: {{ deltaDays(user.last_connection) }} days</p>
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

	[data_title]:hover:after {
		opacity: 1;
		transition: all 0.2s ease 0.6s;
		visibility: visible;
	}
	[data_title]:after {
		content: attr(data_title);
		font-size: 0.6em;
		position: absolute;
		display: flex;
		padding: 4px 8px 4px 8px;
		color: #222;
		background-color: #fff;
		border-radius: 5px;
		box-shadow: 0px 0px 15px #222;
		background-image: -webkit-linear-gradient(
							top, #f8f8f8, #cccccc);

		background-image: -moz-linear-gradient(
							top, #f8f8f8, #cccccc);

		background-image: -ms-linear-gradient(
							top, #f8f8f8, #cccccc);

		background-image: -o-linear-gradient(
							top, #f8f8f8, #cccccc);

		visibility: hidden;
	}
</style>

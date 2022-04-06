<template>
	<div class="grid h-full place-items-center justify-cente gap-x-8 gap-y-4 lg:grid-cols-4 p-8">
		<div class="max-w-md bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl" v-for="(user, index) in users" :key="index">
			<div class="md:flex">
				<div class="md:shrink-0">
				<img class="h-48 w-full object-cover md:h-full md:w-48" :src="urlImg=user.image_url">
				</div>
				<div class="p-8">
				<div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">{{ user.login }}</div>
				<p class="mt-2 text-slate-500">Email: {{ user.email }}</p>
				<p class="mt-2 text-slate-500">Days Left: {{ user.days_left }}</p>
				<p class="mt-2 text-slate-500">Last connexion: {{ convert_date(user.last_connection) }}</p>
				</div>
			</div>
			</div>
	</div>
</template>

<script>
	import axios from 'axios'

	export default {
		name: 'ListUser',
		data() {
			return {
				users: [],
				new_date: '',
			}
		},
		methods: {
			convert_date: function(str_date) {
				this.new_date = new Date(str_date).toUTCString().split(' ').slice(0, 4).join(' ')

				return this.new_date
			}

		},
		mounted() {
			axios
			.get('http://localhost:5280/users/blackhole-timeout', {
				headers: {
					"Access-Control-Allow-Origin": "*"
				},
				params: {
					page: 1
				}
			})
			.then(response => {
				console.log(response.data.data)
				this.users = response.data.data;
			})
		}
	}
</script>

<style>
	.avatard {
		background-size: cover;
	}
</style>

<template>
	<div class="users-bh">
		<ul class="grid h-full place-items-center justify-cente gap-x-8 gap-y-4 lg:grid-cols-2 2xl:grid-cols-3 3xl:grid-cols-4 p-8">
			<li class="max-w-md bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl" v-for="(user, index) in users" v-bind:key="index">
				<item-user :user=user :convertDate=convertDate></item-user>
			</li>
		</ul>
	</div>
</template>

<script>
	import axios from 'axios'
	import ItemUser from './ItemUser.vue'

	export default {
		name: 'BlackholeView',
		data() {
			return {
				users: [],
				page_index: 1
			}
		},
		methods: {
			convertDate: function(str_date) {
				return new Date(str_date).toUTCString().split(' ').slice(0, 4).join(' ');
			},
			logger: function(trace) {
				console.log(trace);
			},
			getUsers: function() {
				axios
				.get('http://localhost:5280/users/blackhole-timeout', {
					headers: {
						"Access-Control-Allow-Origin": "*"
					},
					params: {
						page: this.page_index
					}
				})
				.then(response => {
					console.log(response.data.data);
					this.users.push(...response.data.data);
					this.page_index++;
				});
			}
		},
		components: {
			'item-user': ItemUser
		},
		mounted() {
			this.getUsers();
		}
	}
</script>

<style>
</style>

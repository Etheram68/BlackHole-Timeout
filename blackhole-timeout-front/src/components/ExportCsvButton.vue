<template>
	<div class="flex flex-row-reverse mr-5">
		<button class="relative px-5 py-3 overflow-hidden font-medium text-white bg-cyan-500 border border-cyan-100 rounded shadow-inner group">
			<span class="absolute top-0 left-0 w-0 h-0 transition-all duration-200 border-t-2 border-gray-600 group-hover:w-full ease"></span>
			<span class="absolute bottom-0 right-0 w-0 h-0 transition-all duration-200 border-b-2 border-gray-600 group-hover:w-full ease"></span>
			<span class="absolute top-0 left-0 w-full h-0 transition-all duration-300 delay-200 bg-gray-600 group-hover:h-full ease"></span>
			<span class="absolute bottom-0 left-0 w-full h-0 transition-all duration-300 delay-200 bg-gray-600 group-hover:h-full ease"></span>
			<span class="absolute inset-0 w-full h-full duration-300 delay-300 bg-gray-900 opacity-0 group-hover:opacity-100"></span>
			<span class="relative transition-colors duration-300 delay-200 group-hover:text-white ease inline-flex rounded-md" v-on:click="getCsv()">
				<svg ref="spin" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" v-show="spin_hidden">
					<circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
					<path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
				</svg>
				{{ message_export }}
			</span>
		</button>
	</div>
</template>

<script>
	export default {
		name: 'ExportCsvButton',
		data() {
			return {
				message_export: "Export to CSV",
				spin_hidden: false,
			}
		},
		methods: {
			getCsv: function() {
				this.message_export = 'Exporting...';
				this.spin_hidden = true;
			}
		}
	}
</script>

<style scoped>
</style>

<template>
    <div class="users-bh" ref="users_bh">
        <div class="flex flex-row-reverse mr-5">
            <button href="#_" class="relative px-5 py-3 overflow-hidden font-medium text-white bg-cyan-500 border border-cyan-100 rounded shadow-inner group">
                <span class="absolute top-0 left-0 w-0 h-0 transition-all duration-200 border-t-2 border-gray-600 group-hover:w-full ease"></span>
                <span class="absolute bottom-0 right-0 w-0 h-0 transition-all duration-200 border-b-2 border-gray-600 group-hover:w-full ease"></span>
                <span class="absolute top-0 left-0 w-full h-0 transition-all duration-300 delay-200 bg-gray-600 group-hover:h-full ease"></span>
                <span class="absolute bottom-0 left-0 w-full h-0 transition-all duration-300 delay-200 bg-gray-600 group-hover:h-full ease"></span>
                <span class="absolute inset-0 w-full h-full duration-300 delay-300 bg-gray-900 opacity-0 group-hover:opacity-100"></span>
                <span class="relative transition-colors duration-300 delay-200 group-hover:text-white ease inline-flex rounded-md">
                    <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Export to CSV
                </span>
            </button>
        </div>
        <ul class="grid h-full place-items-center justify-cente gap-x-8 gap-y-4 lg:grid-cols-2 2xl:grid-cols-3 3xl:grid-cols-4 p-8">
            <li class="max-w-md bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl" v-for="(user, index) in users" v-bind:key="index">
                <item-user :user=user :convertDate=convertDate :deltaDays=deltaDays></item-user>
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
            deltaDays: function(str_date) {
                let date_now = new Date().getTime();
                let date = new Date(str_date).toUTCString().split(' ').slice(0, 4).join(' ')
                date = Date.parse(date);
                return Math.ceil(Math.abs(date - date_now) / (1000 * 60 * 60 * 24))
            },
            calcNumberItemsPages: function() {
                if (window.innerWidth >= 1890)
                    return 28;
                else if (window.innerWidth >= 1536)
                    return 21;
                else if (window.innerWidth >= 1024)
                    return 16;
                else if (window.innerWidth >= 768)
                    return 10;
                else
                    return 8;
            },
            getUsers: function() {
                axios
                .get('http://localhost:5280/users/blackhole-timeout', {
                    headers: {
                        "Access-Control-Allow-Origin": "*"
                    },
                    params: {
                        page: this.page_index,
                        nb_per_page: this.calcNumberItemsPages()
                    }
                })
                .then(response => {
                    console.log(response.data.data);
                    this.users.push(...response.data.data);
                    this.page_index++;
                });
            },
            handleScroll: function() {
                if (this.$refs.users_bh.getBoundingClientRect().bottom <= window.innerHeight)
                    this.getUsers();
            }
        },
        components: {
            'item-user': ItemUser
        },
        mounted() {
            this.getUsers();
            window.addEventListener("scroll", this.handleScroll)
        },
        unmounted() {
            window.removeEventListener("scroll", this.handleScroll)
        }
    }
</script>

<style scoped>

</style>

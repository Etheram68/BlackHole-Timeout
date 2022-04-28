<template>
    <div class="users-bh" ref="users_bh">
        <export-csv-button></export-csv-button>
        <ul class="grid h-full place-items-center justify-cente gap-x-8 gap-y-4 lg:grid-cols-2 2xl:grid-cols-3 3xl:grid-cols-4 p-8">
            <li class="max-w-md bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl dark:dark:dark:bg-slate-600" v-for="(user, index) in users" v-bind:key="index">
                <item-user :user=user :convertDate=convertDate :deltaDays=deltaDays></item-user>
            </li>
        </ul>
    </div>
</template>

<script>
    import axios from 'axios'
    import ItemUser from './ItemUser.vue'
    import ExportCsvButton from './ExportCsvButton.vue'

    export default {
        name: 'BlackholeView',
        data() {
            return {
                users: [],
                page_index: 1,
            }
        },
        methods: {
            convertDate: function(str_date) {
                return new Date(str_date).toString().split(' ').slice(0, 4).join(' ');
            },
            deltaDays: function(str_date) {
                let date_now = new Date().getTime();
                let date = new Date(str_date).toString().split(' ').slice(0, 4).join(' ');
                date = Date.parse(date);
                return Math.ceil(Math.abs(date - date_now) / (1000 * 60 * 60 * 24)) - 1
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
                    // console.log(response.data.data);
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
            'item-user': ItemUser,
            'export-csv-button': ExportCsvButton,
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

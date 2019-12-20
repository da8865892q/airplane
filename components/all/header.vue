
<template>
    <div>
        <h1 style="text-align:center" ><nuxt-link to="/">Airplane</nuxt-link></h1>
        <div id="menu-wrapper">
            <div id="menu" class="container">
                <ul>
                    <li class="current_page_item"><nuxt-link to="/" >首頁</nuxt-link></li>
                        <li><nuxt-link to="/infomation">機場/航空公司</nuxt-link></li>
                        <li><nuxt-link to="/flight">航班查詢</nuxt-link></li>
                        <li><a href="schedule.html">時刻表查詢</a></li>
                        <li><a href="about.html">關於我們</a></li>
                        <li><a href="contact.html">聯絡我們</a></li>
                    </ul>
            </div>
        </div>
    </div>
</template>
<script>


export default {
  components: {
  }
}
</script>

<style>

</style>

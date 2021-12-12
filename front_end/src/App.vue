<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <div>
        <div class="header">
            <h1 class="title">东九室内地图</h1>
        </div>

        <div class="topnav">
            <a href="#">RSS指纹可视化</a>
            <a href="#">RSS指纹定位</a>
        </div>
        
        <div class="row">
            <div class="column1">
                <div class="map">
                    <!-- <p> -->
                        <!-- <div id="container" style="width: 600px;height:400px;"></div> -->
                        <!-- <div id="container" style="height: 100%;margin: 0;"></div>
                        <script type = "text/javascript" src="./javascript/map.js"></script> -->
                        <img src="./assets/img/DJ室内布局图.svg" usemap="#image-map">

                        <map name="image-map">
                            <!-- <area v-for="item in rssList" :key="item.id" target="" alt="" v-bind:title="item.rss" href="" v-bind:coords="(parseInt(19.5*item.ylabel+107.7),parseInt(-20*item.xlabel+616.6),parseInt(19.5*item.ylabel+107.7)+6,parseInt(-20*item.xlabel+616.6))" shape="rect" style="background-color:#00000070"/> -->
                            <area v-for="item in rssList" :key="item.id" target="" alt="" v-bind:title="item.rss" href="" v-bind:coords="parseInt(19.5*item.ylabel+107.7)+','+parseInt(-20*item.xlabel+616.6)+','+5" shape="circle"/>
                        </map>

                    <!-- </p> -->
                </div>
                
            </div>
            <div class="column2">
                <div class="choice">
                    <a href="#">添加RSS指纹</a>
                </div>
                <div class="choice">
                    <a href="#">删除RSS指纹</a>
                </div>
                <div class="choice">
                    <a href="#">修改RSS指纹</a>
                </div>
            </div>
        </div>

        <!-- <div>
            <input  type="file" ref="refFile" v-on:change="importCsv">
        </div> -->

        <!-- <div class="update">
            <button class="buttons" @click = 'find'>更新室内地图</button>
        </div> -->

        <div class="footer">
            <p>@电信1901 胡润龙 付丁捷</p>
        </div>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'
 
export default {
  name: 'App',
  components: {
    // HelloWorld
  },
  data(){
    return{
      rssList:[],
      x1:525,
    }
  },
  mounted(){
    this.getRssList()
  },
  methods:{
    getRssList(){
      axios({
        url:"http://127.0.0.1:9000/get-rss-list/",
        type:'json',
        method:'get'
      }).then((res)=>{
        console.log(res)
        this.rssList = res.data
      })
    }
  }
}
</script>

<style>
.header{
    background-color: #f1f1f1;
    padding: 20px;
    text-align: center;
}

.topnav{
    overflow: hidden;
    background-color: #333;
}

.topnav a{
    float: left;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

.topnav a:hover{
    background-color: #ddd;
    color: black;
}

.row:after {
    content: "";
    display: table;
    clear: both;
  }

.column1{
    background-color: #f1f1f1;
    float: left;
    width: 80%;
}

.column2{
    background-color: #333  ;
    float: right;
    width: 20%;
    height: 1163px;
}

.map{
    text-align: center;
}

.choice{
    overflow: hidden;
    background-color: #333;
    width: 100%;
}

.choice a{
    float: center;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;   
}

.update{
    float: center;
    overflow: hidden;
    background-color: #333;
    width: 100%;
}

.buttons{
    overflow: hidden;
    float: center;
    display: block;
    background-color: #333;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    width: 100%;
}
/* .choice button{
    float: center;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
} */

.choice a:hover{
    background-color: #ddd;
    color: black;    
}

.footer {
    background-color: #333;
    padding: 10px;
    text-align: center;
    color: #ddd;
  }

.area{
    background-color: #333;
    color: #333;
}
</style>

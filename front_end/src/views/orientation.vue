<template>
  <div class="orientation">
    <div class="RSS">
        <span>RSS指纹:</span>
        <input v-model="rss" type="text" placeholder="输入RSS"/>
    </div>
    <div class="positon">Prediction: {{location}}</div>
    <div class="positon1">Real: {{testLocation}}</div>
    <button @click="submit">上传RSS</button> 
    <div class="view" style="position: relative">
        <img src="../assets/img/DJ室内布局图.svg"/>
        <a v-bind:style="'display:block;position:absolute; left:'+parseInt(19.5*location[1]+453.7)+'px;top:'+parseInt(-20*location[0]+616.6)+'px;width:10px;height:10px;background:#fcb70a'"></a>
        <a v-bind:style="'display:block;position:absolute; left:'+parseInt(19.5*testLocation[1]+453.7)+'px;top:'+parseInt(-20*testLocation[0]+616.6)+'px;width:10px;height:10px;background:#63bbd0'"></a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Qs from "qs"

export default {
    name:"orientation" ,
    data(){
        return{
            rss:"",
            location:[],
            rssList:[],
            testLocation:[]
        }
    },
    mounted(){
    },
    methods:{
        submit(){
            console.log(this.rss)
            var rss = this.rss
            if(rss.length > 0){
                axios({
                    url:'http://127.0.0.1:9000/orientation/',
                    data:Qs.stringify({
                        rss
                    }),
                    method:'post',
                    headers:{
                        "Content-Type":"application/x-www-form-urlencoded"
                    }
                }).then((res)=>{
                    console.log(res);
                    this.location = res.data[0]
                    this.testLocation = res.data[1]
                })
            }
        }, 
    }  
}
</script>

<style>
.orientation .view img{
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>


<template>
  <div class="orientation">
    <div class="RSS">
        <span>RSS指纹:</span>
        <input v-model="rss" type="text" placeholder="输入RSS"/>
    </div>
    <div class="positon">{{location}}</div>
    <button @click="submit">上传RSS</button>
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
            location:[]
        }
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
                    this.location = res.data
                })
            }
        },
    }  
}
</script>

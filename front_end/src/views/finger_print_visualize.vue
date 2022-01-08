<template>
  <div class="finger-print-visualize">
    <button v-if="controlNow == 'add'" @click="controlSwitch('add')" style="color:#ffffff">add</button>
    <button v-else @click="controlSwitch('add')">add</button>
    <button v-if="controlNow == 'update'" @click="controlSwitch('update')" style="color:#ffffff">update</button>
    <button v-else @click="controlSwitch('update')">update</button>
    <button v-if="controlNow == 'delete'" @click="controlSwitch('delete')" style="color:#ffffff">delete</button>
    <button v-else @click="controlSwitch('delete')">delete</button>
    <div v-if="controlNow != 'default'&& controlNow != 'delete'" class="updateArea">
      <div v-for="(item,index) in tableHead" :key="item.id">
        <label v-if="item != '操作'">{{item}}</label>
        <input v-if="item != '操作'" type="text" class="form-control" v-model="updateData[index]"/>
      </div>
      <button v-if="controlNow == 'add'" @click="add()">Add</button>
    </div>
    <div class="view">
      <table class="table">
        <br/>
        <thead>
          <tr>
            <th v-for="item in tableHead" :key=item.id>{{item}}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="data in tableContent" :key="data.id">
            <td v-for="item in data" :key="item.id">{{item}}</td>
            <button @click="update(data.id)">update</button>
            <button @click="deleteData(data.id)">delete</button>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'

export default({
  data(){
    return{
      tableHead:['id','p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30','xlabel','ylabel','操作'],
      tableContent:[],
      updateData:['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
      controlNow:''
    }
  },
  mounted(){
    this.getTestTable()
    this.controlNow = 'default'
  },
  methods:{
    getTestTable(){
      axios({
        url:"http://127.0.0.1:9000/get-test-list/",
        type:"json",
        method:"get"
      }).then((res)=>{
        this.tableContent = res.data
      })
    },
    update(id){
      var updateData = this.updateData
      axios({
        url:"http://127.0.0.1:9000/update-test-list/",
        data:
          Qs.stringify({
            id,
            updateData
          }),
        method:'post',
        headers:{
            "Content-Type":"application/x-www-form-urlencoded"
        },
        type:"json"
      }).then((res)=>{
        console.log(res),
        this.getTestTable()
        this.controlSwitch('default')
      })
    },
    controlSwitch(control){
      if(this.controlNow == control){
        this.controlNow = 'default'
      }
      else{
        this.controlNow = control
      }
    },
    deleteData(id){
      var controlNow = this.controlNow
      if(controlNow != 'delete')
        alert('Please confirm before you delete!')
      axios({
        url:"http://127.0.0.1:9000/delete-test-list/",
        data:
          Qs.stringify({
            id,
            controlNow          
          }),
        method:'delete',
        headers:{
            "Content-Type":"application/x-www-form-urlencoded"
        },
        type:"json"
      }).then((res)=>{
        console.log(res),
        this.getTestTable()
      })
    },
    add(){
      var updateData = this.updateData
      for(var i=0; i < 33; i++){
        if(updateData[i] == ''){
          alert('Blank features exists!');
          return;
        }
      }
      axios({
        url:"http://127.0.0.1:9000/add-test-list/",
        data:
          Qs.stringify({
            updateData
          }),
        method:'post',
        headers:{
            "Content-Type":"application/x-www-form-urlencoded"
        },
        type:"json"
      }).then((res)=>{
        console.log(res),
        this.getTestTable()
        this.controlSwitch('default')
      })
    }
  }
})
</script>

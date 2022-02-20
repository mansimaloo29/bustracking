var config = {
    apiKey: "AIzaSyDVif5V-QEaMfDuMa8TvVxWg6DTMpZDSyQ",
    authDomain: "tracking-2fa5f.firebaseapp.com",
    databaseURL:"https://tracking-2fa5f-default-rtdb.firebaseio.com",
    projectId: "tracking-2fa5f",
    storageBucket: "tracking-2fa5f.appspot.com",
    messagingSenderId: "156615559135",
    
};
 
  var db = firebase.initializeApp(config).database();
  var currentVal ;
  var { LMap, LTileLayer, LMarker } = Vue2Leaflet;
  var userRefs = db.ref('users')
  
  function myFunction() {
  var x = document.getElementById("myNumber");
  var defaultVal = x.defaultValue;
 currentVal = x.value;
  console.log(currentVal);
  // localStorage.setItem
 
 if(currentVal != undefined){
  new Vue({
    el: '#app',
    components: { LMap, LTileLayer, LMarker },
    data() {
      return {
        
        myUuid : localStorage.getItem('myUuid'),
        zoom:13,
        center: L.latLng(47.413220, -1.219482),
        url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
        attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        marker: L.latLng(47.413220, -1.219482),
        watchPositionId : null
      }
    },
    mounted(){
      var vm = this
      if (!vm.myUuid) {
        vm.myUuid = vm.guid();
        localStorage.setItem('myUuid', vm.myUuid);
        console.log(d)
      }else{
        
        vm.watchPositionId = navigator.geolocation.watchPosition(vm.successCoords, vm.errorCoords);
        
      }
      
      
      
    },
    firebase: {
      users: userRefs.limitToLast(25)
    },
    methods:{
      successCoords(position) {
        var vm = this
        // var busNum = document.getElementById("busno").value;
        //myFunction();
        console.log(currentVal);

        if (!position.coords) return
        
        userRefs.child(currentVal).set({
          coords: {
            latitude: position.coords.latitude,
            longitude: position.coords.longitude,
           
          },
          timestamp: Math.floor(Date.now() / 1000),
        },)
        vm.center = L.latLng([position.coords.latitude, position.coords.longitude])
        vm.marker = L.latLng([position.coords.latitude, position.coords.longitude])

      },
      formatLocation(lat, lng){
        return L.latLng(lat,lng)
      },
      errorCoords() {
        console.log('Unable to get current position')
      },
      guid() {
        function s4() {
          return Math.floor((1 + Math.random()) * 0x10000).toString(16).substring(1);
        }
        return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4();
      }
    }
  });
  
}
else{
  console.log("undefinedddddddddddddddddddd")
}
}
console.log(currentVal)
  var ref = firebase.database().ref(currentVal);

ref.on("value", function(snapshot) {
   console.log(snapshot.val());
}, function (error) {
   console.log("Error: " + error.code);
});

function submitData(data){
  console.log(data);
  var d = data;
}
function toggleDiv() {
  console.log("Inside function")
  var x = document.getElementById("dvMap");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

// var currentVal ;


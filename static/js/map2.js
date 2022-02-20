// var config = {
//     apiKey: "AIzaSyDEuX4A78S5txhl1T-SsM7WBBMkFJIXmPk",
//     authDomain: "maps-4d585.firebaseapp.com",
//     databaseURL: "https://maps-4d585-default-rtdb.firebaseio.com",
//     projectId: "maps-4d585",
//     storageBucket: "maps-4d585.appspot.com",
//     messagingSenderId: "98884066017"
//   };
var config = {
    apiKey: "AIzaSyDVif5V-QEaMfDuMa8TvVxWg6DTMpZDSyQ",
    authDomain: "tracking-2fa5f.firebaseapp.com",
    databaseURL:"https://tracking-2fa5f-default-rtdb.firebaseio.com",
    projectId: "tracking-2fa5f",
    storageBucket: "tracking-2fa5f.appspot.com",
    messagingSenderId: "156615559135",
    
};
var db = firebase.initializeApp(config).database();

var { LMap, LTileLayer, LMarker } = Vue2Leaflet;
var userRefs = db.ref('users')
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
    }else{
      
      vm.watchPositionId = navigator.geolocation.watchPosition(vm.successCoords, vm.errorCoords);
      
    }
    
    
    
  },
  firebase: {
    users: userRefs
  },
  methods:{
    successCoords(position) {
      var vm = this
      if (!position.coords) return
      
      userRefs.child(vm.myUuid).set({
        coords: {
          latitude: position.coords.latitude,
          longitude: position.coords.longitude,
        },
        timestamp: Math.floor(Date.now() / 1000)
      })
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
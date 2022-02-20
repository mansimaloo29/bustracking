var busNo;
function details(No){
	console.log(No)
    busNo = No

var config = {
    apiKey: "AIzaSyDVif5V-QEaMfDuMa8TvVxWg6DTMpZDSyQ",
    authDomain: "tracking-2fa5f.firebaseapp.com",
    databaseURL:"https://tracking-2fa5f-default-rtdb.firebaseio.com",
    projectId: "tracking-2fa5f",
    storageBucket: "tracking-2fa5f.appspot.com",
    messagingSenderId: "156615559135",
    
};
var map = new google.maps.Map(
            document.getElementById("map_canvas"), {
            center: new google.maps.LatLng(37.4419, -122.1419),
            zoom: 13,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });
var db = firebase.initializeApp(config).database()
if(busNo != undefined){
 var userRefs = db.ref('users')
  var locationsRef = firebase.database().ref('users').child(busNo).child('coords');
  //var bounds = new google.maps.LatLngBounds();
   locationsRef.on("value", function(snapshot) {
   console.log(snapshot.val());
var data = snapshot.val();
     var marker = new google.maps.Marker({
                position: {
                    lat: data.lat,
                    lng: data.lng
                },
                map: map,
                label: {
                    color: 'white',
                    fontWeight: 'bold',
                    
                }
                });
 });
}else{
	console.log("UNDEFINED")
}
}
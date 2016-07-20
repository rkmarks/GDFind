var apiGeolocationSuccess = function(position) {
    jQuery('[name=lat]').val(latitude);
    jQuery('[name=lon]').val(longitude);
	alert("API geolocation success!\n\nlat = " + position.coords.latitude + "\nlng = " + position.coords.longitude);
};

var tryAPIGeolocation = function() {
	jQuery.post( "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDCa1LUe1vOczX1hO_iGYgyo8p_jYuGOPU", function(success) {
		apiGeolocationSuccess({coords: {latitude: success.location.lat, longitude: success.location.lng}});
  })
  .fail(function(err) {
    alert("API Geolocation error! \n\n"+err);
  });
};

var browserGeolocationSuccess = function(position) {
    jQuery('[name=lat]').val(latitude);
    jQuery('[name=lon]').val(longitude);
	alert("Browser geolocation success!\n\nlat = " + position.coords.latitude + "\nlng = " + position.coords.longitude);
};

var browserGeolocationFail = function(error) {
  switch (error.code) {
    case error.TIMEOUT:
      alert("Browser geolocation error !\n\nTimeout.");
      break;
    case error.PERMISSION_DENIED:
      if(error.message.indexOf("Only secure origins are allowed") == 0) {
        tryAPIGeolocation();
      }
      break;
    case error.POSITION_UNAVAILABLE:
      alert("Browser geolocation error !\n\nPosition unavailable.");
      break;
  }
};

var tryGeolocation = function() {
  var output = document.getElementById("out");

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
    	browserGeolocationSuccess,
      browserGeolocationFail,
      {maximumAge: 50000, timeout: 20000, enableHighAccuracy: true});
  }else{
    output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
  }
};

tryGeolocation();

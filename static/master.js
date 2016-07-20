var apiGeolocationSuccess = function(position) {
	alert("API geolocation success!\n\nlat = " + position.coords.latitude + "\nlng = " + position.coords.longitude);
};

var tryAPIGeolocation = function() {
	jQuery.post( "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyAk7b9MJIx55VInscuoRW008MhC_XA78wA", function(success) {
		apiGeolocationSuccess({coords: {latitude: success.location.lat, longitude: success.location.lng}});
  })
  .fail(function(err) {
    alert("API Geolocation error! \n\n"+err);
  });
};

var browserGeolocationSuccess = function(position) {
    var latitude  = position.coords.latitude;
    var longitude = position.coords.longitude;
    var latlon = latitude+','+longitude;

    jQuery.getJSON("https://maps.googleapis.com/maps/api/geocode/json?latlng=" +
        latlon+"&key=AIzaSyAk7b9MJIx55VInscuoRW008MhC_XA78wA", function (data) {
		var address = data.results[0].address_components;
		var zipcode = address[address.length - 1].long_name;
		jQuery('[name=zipcode]').val(zipcode);
    });
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
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
    	browserGeolocationSuccess,
      browserGeolocationFail,
      {maximumAge: 50000, timeout: 20000, enableHighAccuracy: true});
  }
};

tryGeolocation();

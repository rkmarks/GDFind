function geoFindMe() {
  var output = document.getElementById("out");

  if (!navigator.geolocation){
    output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
    return;
  }

  function success(position) {

    var latitude  = position.coords.latitude;
    var longitude = position.coords.longitude;
    jQuery('[name=lat]').val(latitude);
    jQuery('[name=lon]').val(longitude);

    var latlon = latitude+','+longitude;

    //output.innerHTML = '<p>Latitude is ' + latitude + '° <br>Longitude is ' + longitude + '°</p>';

    jQuery.getJSON("https://maps.googleapis.com/maps/api/geocode/json?latlng=" +
        latlon+"&key=AIzaSyAfpUjvQXuQFyHvdClznSTXw5oORrB_Vqs", function (data) {
        $.each(data.results[0].address_components, function (i, item) {
            if(item.types[0] == 'postal_code') {
                jQuery('[name=zip]').val(item.long_name);
            }
        });
     });
/*
    var img = new Image();
    img.src = "https://maps.googleapis.com/maps/api/staticmap?center=" + latitude + "," + longitude +
        "&zoom=13&size=300x300&sensor=false&key=AIzaSyDGqXHYlUaKyesmlbCN0mF-Rf9pZaV6vLM";

    output.appendChild(img);
*/
    output.innerHTML = "";
  }

  function error() {
    output.innerHTML = "Unable to retrieve your location";
  }


    if ("" === jQuery('[name=zip]').val()) {
        output.innerHTML = "<p>Locating…</p>";
        navigator.geolocation.getCurrentPosition(success, error);
    }

}

$(document).ready(function() {
    var myApiKey = 'a7fe0334733ffa3edd9421e2355a6425';
    var appID = '7971b25a';
    var year;
    var month;
    var day;
    var display_info = {};
    var relevant_info = [];

    $('#give_me').click(function () {
        var airline = $('#airline').val();
        var flight_num = $('#flight_num').val();
        year = $('#year').val();
        month = $('#month').val();
        day = $('#day').val();

        $.ajax({
            url: 'https://api.flightstats.com/flex/flightstatus/rest/v2/jsonp/flight/status/' + airline + '/' + flight_num + '/dep/' + year + '/' + month + '/' + day + '?appId=' + appID + '&appKey=' + myApiKey,
            type: 'GET',
            dataType: 'jsonp',
            success: function (data) {
                console.log(data);
                for (i = 0; i < data.flightStatuses.length; i++) {
                    display_info = {};
                    display_info.arrival_airport = data.flightStatuses[i].arrivalAirportFsCode;
                    display_info.departure_airport = data.flightStatuses[i].departureAirportFsCode;
                    display_info.status = data.flightStatuses[i].status;
                    relevant_info.push(display_info);
                    if (data.flightStatuses[i].hasOwnProperty('delays')) {
                        $('#display').append("<div><p>" + "Departure Airport: " + display_info.departure_airport + "<br>"
                            + "Arrival Airport: " + display_info.arrival_airport + "<br>" + "Delayed Minutes: "
                            + data.flightStatuses[i].delays.departureGateDelayMinutes + "</p></div>");
                        $('#minutes').append("Flight is delayed for: " + "<br>" + data.flightStatuses[i].delays.departureGateDelayMinutes
                            + " minutes" + "<br>");
                        $('#flightModal').modal('show');
                    }
                    else {
                        $('#display').append("<div><p>" + " Departure Airport: " + display_info.departure_airport + "<br>"
                            + " Arrival Airport: " + display_info.arrival_airport + "<br>" + " Current Flight Status: "
                            + display_info.status + "<br>" + "</p></div>");
                        $('#flightModal1').modal('show');
                    }
                }
            },
            error: function (error_message) {
                console.log(error_message);
            }
        });


//        $('.message').click(function () {
//            $('#creepin').modal('show');
//        });
//
//        $('#message1').click(function () {
//            $('#creepin1').modal('show');
//        });
//
//        $('#message2').click(function () {
//            $('#creepin2').modal('show');
//        });


        //////////ADDING GEOLOCATION TO FIGURE OUT WHICH AIRPORT USER BELONGS TO

        var latitude;
        var longitude;

        Number.prototype.toRad = function () {
            return this * (Math.PI / 180);
        };

        // SUCCESS FUNCTION TO GET USER PERMISSION FOR CURRENT LATITUDE & LONGITUDE
        function success(position) {
            latitude = Number(position.coords.latitude);
            console.log("LATITUDE: " + latitude);
            longitude = Number(position.coords.longitude);
            console.log("LONGITUDE: " + longitude);

        }

        // CHECK TO SEE IF GEOLOCATION EXISTS
        if (navigator.geolocation) {
            console.log("Geolocation found, getting coordinates now...");
            navigator.geolocation.getCurrentPosition(success, error);
        } else {
            console.log("Geolocation not found, please try again!");
            error("not supported");
        }

        var coords = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);

        var options = {
            zoom: 15,
            center: coords,
            mapTypeControl: false,
            navigationControlOptions: {
                style: google.maps.NavigationControlStyle.SMALL
            },
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("mapcontainer"), options);

        var marker = new google.maps.Marker({
            position: coords,
            map: map,
            title: "You are here!"
        });

        /////END OF GEOLOCATION CODES

    });
});
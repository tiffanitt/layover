$(document).ready(function(){
    var myApiKey = 'a7fe0334733ffa3edd9421e2355a6425';
    var appID = '7971b25a';
    var year;
    var month;
    var day;
    var display_info = {};
    var relevant_info = [];

    $('#give_me').on('click', function(){
        var airline = $('#airline').val();
        var flight_num = $('#flight_num').val();
        year = $('#year').val();
        month = $('#month').val();
        day = $('#day').val();

        $.ajax({
            url: 'https://api.flightstats.com/flex/flightstatus/rest/v2/jsonp/flight/status/'+ airline +'/'+ flight_num +'/dep/' + year +'/'+ month +'/'+ day +'?appId=' + appID + '&appKey=' + myApiKey,
            type: 'GET',
            dataType: 'jsonp',
            success: function(data){
                console.log(data);
                for (i=0; i<data.flightStatuses.length; i++){
                    display_info={};
                    display_info.arrival_airport=data.flightStatuses[i].arrivalAirportFsCode;
                    display_info.departure_airport=data.flightStatuses[i].departureAirportFsCode;
                    display_info.status=data.flightStatuses[i].status;
                    relevant_info.push(display_info);
                    if (data.flightStatuses[i].hasOwnProperty('delays')) {
                        $('#display').append("<div><p>" + "Departure Airport: " + display_info.departure_airport + "<br>"
                            + "Arrival Airport: " + display_info.arrival_airport + "<br>" + "Delayed Minutes: "
                            + data.flightStatuses[i].delays.departureGateDelayMinutes + "</p></div>");
                        $('#minutes').append("Flight is delayed for: "+ "<br>"+data.flightStatuses[i].delays.departureGateDelayMinutes
                            +" minutes"+"<br>");
                        $('#myModal').modal('show');
                    }
                    else {
                        $('#display').append("<div><p>" + " Departure Airport: "+display_info.departure_airport+ "<br>"
                            +" Arrival Airport: "+display_info.arrival_airport+ "<br>"+" Current Flight Status: "
                            + display_info.status+"<br>"+"</p></div>");
                        $('#myModal2').modal('show');
                    }
                }
            },
            error: function(error_message){
                console.log(error_message);
            }
        })
    });

$('.message').on('click',function(){
    $('#creepin').modal('show');
});

$('#message1').on('click',function(){
    $('#creepin1').modal('show');
});

$('#message2').on('click',function(){
    $('#creepin2').modal('show');
})



});
$(document).ready(function(){
    console.log("ready to go!");
    $('#submit').click(function(){
        var cityChoice = $('#city').val()
        var urlString = "http://api.openweathermap.org/data/2.5/weather?q="+cityChoice;
        urlString += "&APPID=ab5d219c0bafd168444d30ada5673302"
        $.ajax({
            dataType: "json",
            url: urlString,
            success: function(data){
                var temperature = data.main.temp;
                temperature = 9/5 * (temperature - 273) + 32;
                console.log(temperature);
                $('#result').append("It is "+ temperature + "degrees")
            }
          });
    })
})
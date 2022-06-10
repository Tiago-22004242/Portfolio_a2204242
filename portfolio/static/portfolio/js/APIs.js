document.addEventListener('DOMContentLoaded', function () {
        fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
             const owner = data.owner;
             let pais = data.country;
             document.querySelector('#titulo').append(owner + " API");
             document.querySelector('#pais').append("Pais: " + pais);
             let text = "";
             let tMin = data.data[0].tMin;
             let tMax = data.data[0].tMax;
             text += "Temperatura Minima: " + tMin;
             text += " Temperatura Maxima " + tMax;
             document.getElementById('temperaturaSeg').innerHTML = text;
             tMin = data.data[1].tMin;
             tMax = data.data[1].tMax;
             text = "";
             text += "Temperatura Minima: " + tMin;
             text += " Temperatura Maxima " + tMax;
             document.getElementById('temperaturaTer').innerHTML = text;
             tMin = data.data[2].tMin;
             tMax = data.data[2].tMax;
             text = "";
             text += "Temperatura Minima: " + tMin;
             text += " Temperatura Maxima " + tMax;
             document.getElementById('temperaturaQuar').innerHTML = text;
             tMin = data.data[3].tMin;
             tMax = data.data[3].tMax;
             text = "";
             text += "Temperatura Minima: " + tMin;
             text += " Temperatura Maxima " + tMax;
             document.getElementById('temperaturaQui').innerHTML = text;
             tMin = data.data[4].tMin;
             tMax = data.data[4].tMax;
             text = "";
             text += "Temperatura Minima: " + tMin;
             text += " Temperatura Maxima " + tMax;
             document.getElementById('temperaturaSex').innerHTML = text;
        });
        })

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '7b62ebf518msh4d2195104cfd3fcp191794jsnea89a4b3c138',
		'X-RapidAPI-Host': 'covid-193.p.rapidapi.com'
	}
};
	document.addEventListener('DOMContentLoaded', function () {
        fetch('https://covid-193.p.rapidapi.com/statistics?country=Portugal', options)
        .then(response => response.json())
        .then(data => {
             let stats = data.get;
             const country = data.response[0].country
             document.querySelector('#stats').append(stats);
             document.querySelector('#country').append(country);
             let population = data.response[0].population
             document.querySelector('#population').append(population);
             let active = data.response[0].cases.active
             document.querySelector('#active').append(active);
             let critical = data.response[0].cases.critical
             document.querySelector('#critical').append(critical);
             let recovered = data.response[0].cases.recovered
             document.querySelector('#recovered').append(recovered);
             let total = data.response[0].deaths.total
             document.querySelector('#total').append(total);
             let time = data.response[0].time
             document.querySelector('#time').append(time);
        });
        })

        function renderTime() {
        var myDate = new Date();
        var day = myDate.getDate();
        var month = myDate.getMonth();
        var monthArray = ['Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        var year = myDate.getYear();
        if (year < 1000) {
          year += 1900;
        }
        var currentTime = new Date();
        var h = currentTime.getHours();
        var m = currentTime.getMinutes();
        var s = currentTime.getSeconds();

        if (h == 24) {
          h = 0;
        } else if (h > 12) {
          h = h - 0;
        }

        if (h < 10) {
          h = "0" + h;
        }
        if (m < 10) {
          m = "0" + m;
        }
        if (s < 10) {
          s = "0" + s;
        }

        var clock = document.getElementById("relogio");
        clock.textContent = "" + day + " " + monthArray[month] + " " + year + " | " + h + ":" + m + ":" + s;
        clock.innerText = "" + day + " " + monthArray[month] + " " + year + " | " + h + ":" + m + ":" + s;

        setTimeout("renderTime()", 1000)
      }
      renderTime();
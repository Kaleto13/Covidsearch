google.charts.load('current', {'packages':['corechart']});


var DataDP5


function drawChart() {
    var DataDP5
    fetch("./DP5.json")
        .then(res => res.json())
        .then(data => DataDP5 = data)

    var data = google.visualization.arrayToDataTable(DataDP5["Totales"]);

    var Titulo;
    $('.home_content .mapa')[0].addEventListener('load', function() {
        $('.Arica #AricaPath', this.contentDocument).on({
            'mouseenter': function() {
                Titulo = 'Región de Arica y Parinacota';
            },
        });
    }, true);

    var options = {
        hAxis: {title: 'Fechas',  titleTextStyle: {color: '#333'}},
        vAxis: {minValue: 0}
    };

    var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}

google.charts.setOnLoadCallback(drawChart());
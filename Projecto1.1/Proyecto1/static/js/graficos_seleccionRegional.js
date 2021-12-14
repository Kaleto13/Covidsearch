google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawPCRChart);
function drawPCRChart(region) {
    fetch("./DP4.json")
        .then(res => res.json())
        .then(data => DataDP4 = data)
    var data = google.visualization.arrayToDataTable(DataDP4[region]);
    var options = {
        title: 'Total de Contagios Activos.', titleTextStyle: {fontSize: 18},
        hAxis: {title: 'Fechas'},
        vAxis: {title: 'Activos'}, 
        colors: ['#55286f']
        //axes: {x: {0: {side: 'bottom'}}}
    };
    var chart = new google.visualization.AreaChart(document.getElementById('graficos'));
    chart.draw(data, options);
    };

$('#graficos')[0].addEventListener('load', function() {
    $('.Arica #AricaPath', this.contentDocument).on({
        'mouseenter': function() {
        // XV - Región de Arica y Parinacota
        drawPCRChart('XV');
        },
    });
}, true);
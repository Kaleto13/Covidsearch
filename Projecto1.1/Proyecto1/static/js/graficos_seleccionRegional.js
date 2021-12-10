google.charts.load('current', {'packages':['corechart']});


function drawChart() {
    var datos = [
        ['Year', 'Sales'],
        ['2013',  1000],
        ['2014',  1170],
        ['2015',  660],
        ['2016',  1030]
    ]

    var data = google.visualization.arrayToDataTable(datos);

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

google.charts.setOnLoadCallback(drawChart);
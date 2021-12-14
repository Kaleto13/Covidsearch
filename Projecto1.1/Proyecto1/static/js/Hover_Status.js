var nombreRegion = {
    "XV": "Región de Arica y Parinacota",
    "I": "Región de Tarapacá",
    "II": "Región de Antofagasta",
    "III": "Región de Atacama",
    "IV": "Región de Coquimbo",
    "V": "Región de Valparaiso",
    "RM": "Región Metropolitana de Santiago",
    "VI": "Región del Libertador General Bernardo O'Higgins",
    "VII": "Región del Maule",
    "XVI": "Región de Ñuble",
    "VIII": "Región del Biobio",
    "IX": "Región de La Araucanía",
    "XIV": "Región de Los Ríos",
    "X": "Región de Los Lagos",
    "XI": "Región Aysén del General Carlos Ibáñez del Campo",
    "XII": "Región de Magallanes y la Antártica Chilena"
}

var DataDP4, DataPCR, DataDP5;
/*
fetch("./DP4.json")
    .then(res => res.json())
    .then(data => DataDP4 = data)
fetch("./DP7.json")
    .then(res => res.json())
    .then(data => DataPCR = data)
*/
document.getElementById('preview').style.display = 'none';
document.getElementById('menuR').style.display = 'block';


$('.home_content')[0].addEventListener('load', function() {
    $(document).ready(function(){
        $.getJSON('http://127.0.0.1:8000/DP5.json', function(json) {
            DataDP5 = json;
            var num = parseInt(DataDP5["Fallecidos"][10][1]) - parseInt(DataDP5["Fallecidos"][9][1])
            $('.home_content .menuRapido .row4 .semititulo').text("Cifras nacionales del día " + DataDP5["Resumen"][0] + ", MINSAL.")
            $('.home_content .menuRapido .row3 #ContagioTotalNacional').text(DataDP5["Resumen"][1])
            $('.home_content .menuRapido .row .seccionB #ContagiosNuevos').text("+" + DataDP5["Resumen"][4])
            $('.home_content .menuRapido .row .seccionB #CifraActivosNacional').text(DataDP5["Resumen"][3])
            $('.home_content .menuRapido .row .seccionB #Fallecidos').text("+" + num.toString())
            $('.home_content .menuRapido .row .seccionB #CifraFallecidosNacional').text(DataDP5["Resumen"][2])
            $('.home_content .analisis #tituloRegional').text("Cifras regionales del día " + DataDP5["Resumen"][0] + ", MINSAL.")
    
        });
    });
}, true);


function parcheRegional(path, titulo, region){
    $(path, this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(titulo);

            $.getJSON('http://127.0.0.1:8000/DP7.json', function(json) {
                DataPCR = json
                $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR[region][10][1])
            });
            $.getJSON('http://127.0.0.1:8000/DP4.json', function(json) {
                DataDP4 = json
                $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4[region]["Totales"][10][1])
                $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4[region]["Nuevos"][10][1])
                $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4[region]["Activos"][10][1])
            });
            
        },
    });
}

$('.home_content .mapa')[0].addEventListener('load', function() {
    
    // XV - Región de Arica y Parinacota
    parcheRegional('.Arica #AricaPath', nombreRegion['XV'], "XV");
    // I - Región de Tarapacá
    parcheRegional('.Tarapaca #TarapacaPath', nombreRegion['I'], "I");
    // II - Región de Antofagasta
    parcheRegional('.Antofagasta #AntofagastaPath', nombreRegion['II'], "II");
    // III - Región de Atacama
    parcheRegional('.Atacama #AtacamaPath', nombreRegion['III'], "III");
    // IV - Región de Coquimbo
    parcheRegional('.Coquimbo #CoquimboPath', nombreRegion['IV'], "IV");
    // V - Región de Valparaiso
    parcheRegional('.Valparaiso #ValparaisoPath', nombreRegion['V'], "V");
    // RM - Región Metropolitana de Santiago (alias, la peor región de Chile y no es broma.)
    parcheRegional('.Metropolitana #MetropolitanaPath', nombreRegion['RM'], 'RM');
    // VI - Región del Libertador General Bernardo O'Higgins
    parcheRegional('.OHiggins #OHigginsPath', nombreRegion['VI'], "VI");
    // VII - Región del Maule
    parcheRegional('.Maule #MaulePath', nombreRegion['VII'], "VII");
    // XVI - Región de Ñuble
    parcheRegional('.Nuble #NublePath', nombreRegion['XVI'], "XVI");
    // VIII - Región del Biobio
    parcheRegional('.BioBio #BioBioPath', nombreRegion['VIII'], "VIII");
    // IX - Región de La Araucanía
    parcheRegional('.Araucania #AraucaniaPath', nombreRegion['IX'],'IX');
    // XIV - Región de Los Ríos
    parcheRegional('.LosRios #LosRiosPath', nombreRegion['XIV'], "XIV");
    // X - Región del Biobio
    parcheRegional('.LosLagos #LosLagosPath', nombreRegion['X'], "X");
    // XI - Región Aysén del General Carlos Ibáñez del Campo
    parcheRegional('.Aysen #AysenPath', nombreRegion['XI'],"XI");
    // XII - Región de Magallanes y la Antártica Chilena
    parcheRegional('.Magallanes #MagallanesPath', nombreRegion['XII'], 'XII');
}, true);
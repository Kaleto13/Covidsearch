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

fetch("./DP4.json")
    .then(res => res.json())
    .then(data => DataDP4 = data)
fetch("./DP7.json")
    .then(res => res.json())
    .then(data => DataPCR = data)
fetch("./DP5.json")
    .then(res => res.json())
    .then(data => DataDP5 = data)

// ARREGLAR!!!


document.getElementById('preview').style.display = 'none';
document.getElementById('menuR').style.display = 'block';


$('.home_content')[0].addEventListener('load', function() {
    $(document).ready(function(){
        var num = parseInt(DataDP5["Fallecidos"][10][1]) - parseInt(DataDP5["Fallecidos"][9][1])
        $('.home_content .menuRapido .row4 .semititulo').text("Cifras nacionales del día " + DataDP5["Resumen"][0] + ", MINSAL.")
        $('.home_content .menuRapido .row3 #ContagioTotalNacional').text(DataDP5["Resumen"][1])
        $('.home_content .menuRapido .row .seccionB #ContagiosNuevos').text("+" + DataDP5["Resumen"][4])
        $('.home_content .menuRapido .row .seccionB #CifraActivosNacional').text(DataDP5["Resumen"][3])
        $('.home_content .menuRapido .row .seccionB #Fallecidos').text("+" + num.toString())
        $('.home_content .menuRapido .row .seccionB #CifraFallecidosNacional').text(DataDP5["Resumen"][2])
        $('.home_content .analisis #tituloRegional').text("Cifras regionales del día " + DataDP5["Resumen"][0] + ", MINSAL.")
    });
}, true);


function parcheRegional(path, titulo, pcr, totales, nuevos, activos){
    $(path, this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(titulo);
            $('.home_content .analisis .row .seccion #CifraPCR').text(pcr)
            $('.home_content .analisis .row .seccion #CifraTotales').text(totales)
            $('.home_content .analisis .row .seccion #CifraNuevos').text(nuevos)
            $('.home_content .analisis .row .seccion #CifraActivos').text(activos)
        },
    });
}
$('.home_content .mapa')[0].addEventListener('load', function() {
    
    // XV - Región de Arica y Parinacota
    parcheRegional('.Arica #AricaPath', nombreRegion['XV'], "+" + DataPCR["XV"][10][1], DataDP4["XV"]["Totales"][7][1], "+" + DataDP4["XV"]["Nuevos"][7][1], DataDP4["XV"]["Activos"][7][1])
    // I - Región de Tarapacá
    parcheRegional('.Tarapaca #TarapacaPath', nombreRegion['I'], "+" + DataPCR["I"][10][1], DataDP4["I"]["Totales"][7][1], "+" + DataDP4["I"]["Nuevos"][7][1], DataDP4["I"]["Activos"][7][1])
    // II - Región de Antofagasta
    parcheRegional('.Antofagasta #AntofagastaPath', nombreRegion['II'], "+" + DataPCR["II"][10][1], DataDP4["II"]["Totales"][7][1], "+" + DataDP4["II"]["Nuevos"][7][1], DataDP4["II"]["Activos"][7][1])
    // III - Región de Atacama
    parcheRegional('.Atacama #AtacamaPath', nombreRegion['III'], "+" + DataPCR["III"][10][1], DataDP4["III"]["Totales"][7][1], "+" + DataDP4["III"]["Nuevos"][7][1], DataDP4["III"]["Activos"][7][1])
    // IV - Región de Coquimbo
    parcheRegional('.Coquimbo #CoquimboPath', nombreRegion['IV'], "+" + DataPCR["IV"][10][1], DataDP4["IV"]["Totales"][7][1], "+" + DataDP4["IV"]["Nuevos"][7][1], DataDP4["IV"]["Activos"][7][1])
    // V - Región de Valparaiso
    parcheRegional('.Valparaiso #ValparaisoPath', nombreRegion['V'], "+" + DataPCR["V"][10][1], DataDP4["V"]["Totales"][7][1], "+" + DataDP4["V"]["Nuevos"][7][1], DataDP4["V"]["Activos"][7][1])
    // RM - Región Metropolitana de Santiago (alias, la peor región de Chile y no es broma.)
    parcheRegional('.Metropolitana #MetropolitanaPath', nombreRegion['RM'], "+" + DataPCR["RM"][10][1], DataDP4["RM"]["Totales"][7][1], "+" + DataDP4["RM"]["Nuevos"][7][1], DataDP4["RM"]["Activos"][7][1])
    // VI - Región del Libertador General Bernardo O'Higgins
    parcheRegional('.OHiggins #OHigginsPath', nombreRegion['VI'], "+" + DataPCR["VI"][10][1], DataDP4["VI"]["Totales"][7][1], "+" + DataDP4["VI"]["Nuevos"][7][1], DataDP4["VI"]["Activos"][7][1])
    // VII - Región del Maule
    parcheRegional('.Maule #MaulePath', nombreRegion['VII'], "+" + DataPCR["VII"][10][1], DataDP4["VII"]["Totales"][7][1], "+" + DataDP4["VII"]["Nuevos"][7][1], DataDP4["VII"]["Activos"][7][1])
    // XVI - Región de Ñuble
    parcheRegional('.Nuble #NublePath', nombreRegion['XVI'], "+" + DataPCR["XVI"][10][1], DataDP4["XVI"]["Totales"][7][1], "+" + DataDP4["XVI"]["Nuevos"][7][1], DataDP4["XVI"]["Activos"][7][1])
    // VIII - Región del Biobio
    parcheRegional('.BioBio #BioBioPath', nombreRegion['VIII'], "+" + DataPCR["VIII"][10][1], DataDP4["VIII"]["Totales"][7][1], "+" + DataDP4["VIII"]["Nuevos"][7][1], DataDP4["VIII"]["Activos"][7][1])
    // IX - Región de La Araucanía
    parcheRegional('.Araucania #AraucaniaPath', nombreRegion['IX'], "+" + DataPCR['IX'][10][1], DataDP4["IX"]["Totales"][7][1], "+" + DataDP4["IX"]["Nuevos"][7][1], DataDP4["IX"]["Activos"][7][1])
    // XIV - Región de Los Ríos
    parcheRegional('.LosRios #LosRiosPath', nombreRegion['XIV'], "+" + DataPCR['XIV'][10][1], DataDP4["XIV"]["Totales"][7][1], "+" + DataDP4["XIV"]["Nuevos"][7][1], DataDP4["XIV"]["Activos"][7][1])
    // X - Región del Biobio
    parcheRegional('.LosLagos #LosLagosPath', nombreRegion['X'], "+" + DataPCR['X'][10][1], DataDP4["X"]["Totales"][7][1], "+" + DataDP4["X"]["Nuevos"][7][1], DataDP4["X"]["Activos"][7][1])
    // XI - Región Aysén del General Carlos Ibáñez del Campo
    parcheRegional('.Aysen #AysenPath', nombreRegion['XI'], "+" + DataPCR['XI'][10][1], DataDP4["XI"]["Totales"][7][1], "+" + DataDP4["XI"]["Nuevos"][7][1], DataDP4["XI"]["Activos"][7][1])
    // XII - Región de Magallanes y la Antártica Chilena
    parcheRegional('.Magallanes #MagallanesPath', nombreRegion['XII'], "+" + DataPCR['XII'][10][1], DataDP4["XII"]["Totales"][7][1], "+" + DataDP4["XII"]["Nuevos"][7][1], DataDP4["XII"]["Activos"][7][1])
}, true);
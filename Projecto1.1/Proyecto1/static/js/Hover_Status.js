var xlsData = {
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
        $('.home_content .menuRapido .row4 .semititulo').text("Cifras nacionales del día " + DataDP5["Fecha"])
        $('.home_content .menuRapido .row3 #ContagioTotalNacional').text(DataDP5["casostotales"])
        $('.home_content .menuRapido .row .seccionB #ContagiosNuevos').text("+" + DataDP5["casosnuevostotales"])
        $('.home_content .menuRapido .row .seccionB #CifraActivosNacional').text(DataDP5["casosactivos"])
        $('.home_content .menuRapido .row .seccionB #Fallecidos').text("+" + DataDP5["fallecidosnuevos"])
        $('.home_content .menuRapido .row .seccionB #CifraFallecidosNacional').text(DataDP5["fallecidos"])
    });
}, true);

$('.home_content .mapa')[0].addEventListener('load', function() {
    $('.Arica #AricaPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['XV']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["XV"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["XV"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["XV"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["XV"][2])
        },
    });

    $('.Tarapaca #TarapacaPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['I']);
            $('.home_content .analisis .row .seccion #CifraPCR').text(DataPCR["I"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["I"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["I"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["I"][2])
        },
    });

    $('.Antofagasta #AntofagastaPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['II']);    
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["II"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["II"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["II"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["II"][2])        
        },
    });

    $('.Atacama #AtacamaPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['III']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["III"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["III"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["III"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["III"][2])
        },
    });

    $('.Coquimbo #CoquimboPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['IV']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["IV"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["IV"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["IV"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["IV"][2])
        },
    });

    $('.Valparaiso #ValparaisoPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['V']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["V"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["V"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["V"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["V"][2])
        },
    });                    
    
    $('.Metropolitana #MetropolitanaPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['RM']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["RM"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["RM"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["RM"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["RM"][2])
        },
    });     
                        
    $('.OHiggins #OHigginsPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['VI']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["VI"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["VI"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["VI"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["VI"][2])
        },
    });     
    
    $('.Maule #MaulePath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['VII']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["VII"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["VII"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["VII"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["VII"][2])
        },
    });   

    $('.Nuble #NublePath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['XVI']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["XVI"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["XVI"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["XVI"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["XVI"][2])
        },
    });   

    $('.BioBio #BioBioPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['VIII']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["VIII"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["VIII"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["VIII"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["VIII"][2])
        },
    });   

    $('.Araucania #AraucaniaPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['IX']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["IX"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["IV"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["IV"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["IV"][2])
        },
    });   
    
    $('.LosRios #LosRiosPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['XIV']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["XIV"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["XIV"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["XIV"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["XIV"][2])
        },
    });   

    $('.LosLagos #LosLagosPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['X']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["X"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["X"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["X"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["X"][2])
        },
    });  
    
    $('.Aysen #AysenPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['XI']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["XI"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["XI"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["XI"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["XI"][2])
        },
    });   
    $('.LosRios #LosRiosPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['XIV']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["XIV"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["XIV"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["XIV"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["XIV"][2])
        },
    });   

    $('.LosLagos #LosLagosPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['X']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["X"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["X"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["X"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["X"][2])
        },
    });  
    
    $('.Aysen #AysenPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['XI']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["XI"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["XI"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["XI"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["XI"][2])
        },
    });   
        
    $('.Magallanes #MagallanesPath', this.contentDocument).on({
        'mouseenter': function() {
            document.getElementById('preview').style.display = 'block';
            document.getElementById('menuR').style.display = 'none';
            $('.home_content .analisis .titulo').text(xlsData['XII']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("+" + DataPCR["XII"])
            $('.home_content .analisis .row .seccion #CifraTotales').text(DataDP4["XII"][0])
            $('.home_content .analisis .row .seccion #CifraNuevos').text("+" + DataDP4["XII"][1])
            $('.home_content .analisis .row .seccion #CifraActivos').text(DataDP4["XII"][2])
        },
    });   
}, true);
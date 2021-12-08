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

// $('.home_content .analisis .row .seccion #CifraPCR').text("691")
// $('.home_content .analisis .row .seccion #CifraActivos').text("70")
// $('.home_content .analisis .row .seccion #CifraTotales').text("28617")
// $('.home_content .analisis .row .seccion #CifraNuevos').text("9")
 

$('.home_content .mapa')[0].addEventListener('load', function() {
    $('.Arica #AricaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XV']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")

        },
    });

    $('.Tarapaca #TarapacaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['I']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });

    $('.Antofagasta #AntofagastaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['II']);            
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")   
        },
    });

    $('.Atacama #AtacamaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['III']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });

    $('.Coquimbo #CoquimboPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['IV']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });

    $('.Valparaiso #ValparaisoPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['V']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });                    
    
    $('.Metropolitana #MetropolitanaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['RM']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });     
                        
    $('.OHiggins #OHigginsPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['VI']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });     
    
    $('.Maule #MaulePath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['VII']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });   

    $('.Nuble #NublePath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XVI']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });   

    $('.BioBio #BioBioPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['VIII']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });   

    $('.Araucania #AraucaniaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['IX']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });   
    
    $('.LosRios #LosRiosPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XIV']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });   

    $('.LosLagos #LosLagosPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['X']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });  
    
    $('.Aysen #AysenPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XI']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });   
    $('.LosRios #LosRiosPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XIV']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });   

    $('.LosLagos #LosLagosPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['X']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });  
    
    $('.Aysen #AysenPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XI']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });   
        
    $('.Magallanes #MagallanesPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XII']);
            $('.home_content .analisis .row .seccion #CifraPCR').text("691")
        },
    });   
}, true);
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
    "XI": "Región Aysén del General Carlos Ibáñez del Campo"
}

$('.home_content .mapa')[0].addEventListener('load', function() {

    $('.Arica #AricaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XV']);
        },
    });

    $('.Tarapaca #TarapacaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['I']);
        },
    });

    $('.Antofagasta #AntofagastaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['II']);
        },
    });

    $('.Atacama #AtacamaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['III']);
        },
    });

    $('.Coquimbo #CoquimboPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['IV']);
        },
    });

    $('.Valparaiso #ValparaisoPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['V']);
        },
    });                    
    
    $('.Metropolitana #MetropolitanaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['RM']);
        },
    });     
                        
    $('.OHiggins #OHigginsPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['VI']);
        },
    });     
    
    $('.Maule #MaulePath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['VII']);
        },
    });   

    $('.Nuble #NublePath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XVI']);
        },
    });   

    $('.BioBio #BioBioPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['VIII']);
        },
    });   

    $('.Araucania #AraucaniaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['IX']);
        },
    });   
    
    $('.LosRios #LosRiosPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XIV']);
        },
    });   

    $('.LosLagos #LosLagosPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['X']);
        },
    });  
    
    $('.Aysen #AysenPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XI']);
        },
    });   
    $('.LosRios #LosRiosPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XIV']);
        },
    });   

    $('.LosLagos #LosLagosPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['X']);
        },
    });  
    
    $('.Aysen #AysenPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XI']);
        },
    });   
        
    $('.Magallanes #MagallanesPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis .titulo').text(xlsData['XII']);
        },
    });   
}, true);
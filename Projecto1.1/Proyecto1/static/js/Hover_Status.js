var xlsData = {
    "XV - Arica y Parinacota": "Success! Bruh you cracked the code",
}

$('.home_content .mapa')[0].addEventListener('load', function() {

    $('.Arica #AricaPath', this.contentDocument).on({
        'mouseenter': function() {
            $('.home_content .analisis #data').text(xlsData['XV - Arica y Parinacota']);
        },
        'mouseleave': function() {
            $('.home_content .analisis #data').html('');
        }
    });

}, true);
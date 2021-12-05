var xlsData = {
    "XV - Arica y Parinacota": "Success!",
}

$('object')[0].addEventListener('load', function() {

    $('#XV - Arica y Parinacota', this.contentDocument).on({
        'mouseenter': function() {
            $('#hover .data').text(xlsData['XV - Arica y Parinacota']);
        },
        'mouseleave': function() {
            $('#hover .data').html('&nbsp;');
        }
    });

}, true);
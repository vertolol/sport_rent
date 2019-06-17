var city_ajax_url = $('#a_for_city_ajax').attr('href');

$( "#id_region" ).change(function() {

    var id_region

    $( "#id_region option:selected" ).each(function() {
        id_region = $( this ).val();
    });

    $.get( city_ajax_url, {'id_region': id_region}, function( data ) {
        $( "#id_city" ).html( data )
    });

}).trigger( "change" );
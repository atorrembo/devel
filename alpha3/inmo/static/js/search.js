{% extends 'inmo/base.html' %}

{% block content %}

<form method="post" action="./buscador">
    {% csrf_token %}
    <table>
        {{ form }}
    </table>
    <input type="submit" value="Buscar" />
</form>

<script type="text/javascript" src="http://maps.google.com/maps/api/js?key=AIzaSyDSJtOdgDtc7XEfmXd6efs4rDz2E2lAauQ"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script>

    $(document).ready(function() {
        var latlng = new google.maps.LatLng("{{ latitude }}", "{{ longitude }}");
        var mapOptions = {
            zoom: 12,
            center: latlng,
            mapTypeControl: false,
            navigationControlOptions: {style: google.maps.NavigationControlStyle.SMALL},
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        map = new google.maps.Map($('.map')[0], mapOptions);
	var marker = new google.maps.Marker({
            position: latlng,
            map: map,
	    animation: google.maps.Animation.BOUNCE,
            title:"Tu busqueda"
        });

        {% for inmueble in inmuebles %}
            latlng = new google.maps.LatLng( "{{ inmueble.location.y }}" , "{{ inmueble.location.x }}" );
            new google.maps.Marker({
                position: latlng,
                map: map,
                title: "{{ inmueble.titulo }}" 
            });
        {% endfor %}

    console.log('hola');

});


</script>

<div class="map" style="width: 800px; height: 400px;"></div>

{% if inmuebles %}
<h2>Inmuebles en Rango de 2km</h2>
<ul>
    {% for inmueble in inmuebles %}
    <li><b>{{ inmueble.titulo }}</b>: distance: {{ inmueble.distance }}</li>
    {% endfor %}
</ul>
{% endif %}



{% endblock %}

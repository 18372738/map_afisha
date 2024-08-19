from django.shortcuts import render
from .models import Place


def show_index(request):
    places = Place.objects.all()
    payload = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
                },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": "./static/places/moscow_legends.json"
                }
            }for place in places]
    }
    context = {"places" : payload}
    
    return render(request, 'index.html', context)

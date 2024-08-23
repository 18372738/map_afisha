from django.shortcuts import render
from .models import Place
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


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
                "detailsUrl": reverse('location_details', args=[place.id])
                }
            }for place in places]
    }
    context = {"places" : payload}

    return render(request, 'index.html', context)


def location_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    data = {
        "title" : place.title,
        "imgs" : [image.image.url for image in place.name_places.all()],
        "description_short" : place.description_short,
        "description_long" : place.description_long,
        "coordinates" : {
            "lng" : place.lon,
            "lat" : place.lat
        }
    }

    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent' : 2},)

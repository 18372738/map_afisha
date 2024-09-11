from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.urls import reverse

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
                "placeId": place.id,
                "detailsUrl": reverse("location_details", args=[place.id])
            }
        }for place in places]
    }
    context = {"places": payload}

    return render(request, "index.html", context)


def location_details(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related("images"),
        pk=place_id
    )
    payload = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }

    return JsonResponse(
        payload,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )

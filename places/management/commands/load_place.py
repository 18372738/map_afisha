import requests
from django.core.management.base import BaseCommand
from places.models import Place, Picture
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Загрузка данных места в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('file_url', type=str, help='Url-адрес на данные места')


    def handle(self, *args, **kwargs):
        url = kwargs['file_url']
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        place = self.handle_place(data)
        self.handle_picture(data, place)


    def handle_place(self, data):
        place, created = Place.objects.update_or_create(
            title = data['title'],
            description_short = data['description_short'],
            description_long = data['description_long'],
            lat = data['coordinates']['lat'],
            lon = data['coordinates']['lng'],
        )

        return place


    def handle_picture(self, data, place):
        images_url = data['imgs']
        for number, url in enumerate(images_url, 1):
            response = requests.get(url)
            response.raise_for_status()
            image_name = url.split('/')[-1]
            image = ContentFile(response.content, name=image_name)
            image, created = Picture.objects.update_or_create(
                sequence_number = number,
                place = place,
                image = image,
            )

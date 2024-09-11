import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Picture


class Command(BaseCommand):
    help = "Загрузка данных места в базу данных"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_url",
            type=str,
            help="Url-адрес на данные места"
            )

    def handle(self, *args, **kwargs):
        url = kwargs["file_url"]
        response = requests.get(url)
        response.raise_for_status()
        payload = response.json()
        place = self.handle_place(payload)
        self.handle_picture(payload, place)

    def handle_place(self, payload):
        place, created = Place.objects.update_or_create(
            title=payload["title"],
            defaults={
                "short_description": payload["description_short"],
                "long_description": payload["description_long"],
                "lat": payload["coordinates"]["lat"],
                "lon": payload["coordinates"]["lng"],
            }
        )

        return place

    def handle_picture(self, payload, place):
        images_url = payload["imgs"]
        for number, url in enumerate(images_url, 1):
            try:
                response = requests.get(url)
                response.raise_for_status()
                image_name = url.split('/')[-1]
                image = ContentFile(response.content, name=image_name)
                image_obj, created = Picture.objects.update_or_create(
                    sequence_number=number,
                    place=place,
                    defaults={"image": image},
                )

            except HTTPError as http_err:
                print(f"Произошла ошибка при выбое данных{url}: {http_err}")
            except ConnectionError as conn_err:
                print(f"Ошибка подключения {url}: {conn_err}")
            except Exception as err:
                print(f"An error occurred while fetching {url}: {err}")

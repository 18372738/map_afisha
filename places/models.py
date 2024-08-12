from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Картинки', null=True, blank=True)
    description_short = models.TextField('Короткое писнаие', blank=True)
    description_long = models.TextField('Полное описнаие', blank=True)
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")

    def __str__(self):
        return self.title

from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описнаие', blank=True)
    description_long = models.TextField('Полное описнаие', blank=True)
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")

    def __str__(self):
        return self.title


class Picture(models.Model):
    sequence_number = models.IntegerField("Номер картинки", null=True)
    place = models.ForeignKey(Place, verbose_name='Название места', on_delete=models.CASCADE, related_name='name_places')
    image = models.ImageField('Картинка', null=True)

    def __str__(self):
        return f'{self.sequence_number} {self.place.title}'

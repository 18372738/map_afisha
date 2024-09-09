from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200, unique=True)
    short_description = models.TextField('Короткое описнаие', blank=True)
    long_description = HTMLField('Полное описнаие', blank=True)
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")

    def __str__(self):
        return self.title


class Picture(models.Model):
    sequence_number = models.IntegerField(
        verbose_name="Номер картинки",
        default=0,
        db_index=True
    )
    place = models.ForeignKey(
        Place,
        verbose_name='Название места',
        on_delete=models.CASCADE,
        related_name='images')
    image = models.ImageField('Картинка', null=True)

    class Meta:
        ordering = ['sequence_number']

    def __str__(self):
        return f'{self.sequence_number} {self.place.title}'

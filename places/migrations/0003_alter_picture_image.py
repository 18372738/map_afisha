# Generated by Django 4.2.14 on 2024-09-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_picture_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Картинка'),
            preserve_default=False,
        ),
    ]

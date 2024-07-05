# Generated by Django 4.0.6 on 2024-07-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0009_band_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_image',
        ),
        migrations.AddField(
            model_name='music',
            name='lyrics',
            field=models.TextField(default='no lyrics'),
            preserve_default=False,
        ),
    ]
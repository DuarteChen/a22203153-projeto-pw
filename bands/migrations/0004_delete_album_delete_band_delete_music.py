# Generated by Django 4.0.6 on 2024-07-03 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0003_remove_music_writer_delete_bandmember'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Band',
        ),
        migrations.DeleteModel(
            name='Music',
        ),
    ]
# Generated by Django 4.0.6 on 2024-05-23 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_course_conceitosaplicados'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scientificarea',
            name='description',
        ),
    ]

# Generated by Django 4.0.6 on 2024-07-09 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jornalOnline', '0004_alter_article_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='article',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]

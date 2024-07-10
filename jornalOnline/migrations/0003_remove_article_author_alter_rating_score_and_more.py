# Generated by Django 4.0.6 on 2024-07-09 11:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornalOnline', '0002_alter_rating_unique_together_remove_comment_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.DeleteModel(
            name='Journalist',
        ),
    ]
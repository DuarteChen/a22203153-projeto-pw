# Generated by Django 4.0.6 on 2024-07-09 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jornalOnline', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='jornalOnline.journalist'),
        ),
        migrations.RemoveField(
            model_name='rating',
            name='reviewer',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

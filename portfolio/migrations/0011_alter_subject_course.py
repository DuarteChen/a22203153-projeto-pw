# Generated by Django 4.0.6 on 2024-05-23 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_subject_scientificarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.course'),
        ),
    ]
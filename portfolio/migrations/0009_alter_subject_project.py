# Generated by Django 4.0.6 on 2024-05-23 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_concept_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.project'),
        ),
    ]

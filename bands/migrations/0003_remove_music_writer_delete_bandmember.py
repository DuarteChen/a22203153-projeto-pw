# Generated by Django 4.0.6 on 2024-07-03 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0002_remove_bandmember_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='writer',
        ),
        migrations.DeleteModel(
            name='BandMember',
        ),
    ]

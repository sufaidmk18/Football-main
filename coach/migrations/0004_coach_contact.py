# Generated by Django 4.1.7 on 2023-04-03 07:06

from django.db import migrations, models
import player.models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0003_rename_panchayath_coach_village_remove_coach_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='contact',
            field=models.IntegerField(default=0),        ),
    ]

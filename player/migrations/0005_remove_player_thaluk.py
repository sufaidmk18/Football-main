# Generated by Django 4.1.7 on 2023-04-05 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_remove_player_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='thaluk',
        ),
    ]

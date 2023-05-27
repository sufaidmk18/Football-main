# Generated by Django 4.1.6 on 2023-05-20 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0009_player_post'),
        ('coach', '0018_rename_statictics_team_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='track_statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bollcontronl', models.IntegerField(default=50)),
                ('passaccuracy', models.IntegerField(default=50)),
                ('stamina', models.IntegerField(default=50)),
                ('speed', models.IntegerField(default=50)),
                ('takles', models.IntegerField(default=50)),
                ('shoot', models.IntegerField(default=50)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
            ],
        ),
    ]

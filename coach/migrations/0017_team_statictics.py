# Generated by Django 4.1.6 on 2023-05-14 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0016_team_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='statictics',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coach.team_type'),
        ),
    ]
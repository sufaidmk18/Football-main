# Generated by Django 4.1.7 on 2023-04-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0006_remove_coach_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='contact',
            field=models.IntegerField(default=0),
        ),
    ]

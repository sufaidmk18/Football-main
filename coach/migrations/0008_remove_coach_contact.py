# Generated by Django 4.1.7 on 2023-04-03 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0007_coach_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='contact',
        ),
    ]

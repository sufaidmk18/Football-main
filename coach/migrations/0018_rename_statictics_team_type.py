# Generated by Django 4.1.6 on 2023-05-14 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0017_team_statictics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='statictics',
            new_name='type',
        ),
    ]

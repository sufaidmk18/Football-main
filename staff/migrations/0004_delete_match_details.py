# Generated by Django 4.1.7 on 2023-04-05 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_match_remove_match_details_match_remove_staff_photo_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='match_details',
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0008_player_login_alter_player_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='post',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
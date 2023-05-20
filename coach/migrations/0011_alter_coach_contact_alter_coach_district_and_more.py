# Generated by Django 4.1.7 on 2023-04-10 04:55

import coach.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0010_remove_team_match_delete_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='contact',
            field=models.IntegerField(default=coach.models.get_default_value, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='housename',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='place',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='post',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-10 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coach', '0011_alter_coach_contact_alter_coach_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

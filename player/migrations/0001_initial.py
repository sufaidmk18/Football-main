# Generated by Django 4.1.7 on 2023-03-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('contact', models.IntegerField()),
                ('photo', models.FileField(upload_to=None)),
                ('housename', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('panchayath', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
            ],
        ),
    ]

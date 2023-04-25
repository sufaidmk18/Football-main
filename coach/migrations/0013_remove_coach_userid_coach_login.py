# Generated by Django 4.1.7 on 2023-04-10 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_manager_contact'),
        ('coach', '0012_coach_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='userid',
        ),
        migrations.AddField(
            model_name='coach',
            name='login',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.login'),
        ),
    ]

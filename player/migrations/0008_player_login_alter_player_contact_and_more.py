# Generated by Django 4.1.7 on 2023-04-10 05:55

from django.db import migrations, models
import django.db.models.deletion
import player.models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_manager_contact'),
        ('player', '0007_player_coach'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='login',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.login'),
        ),
        migrations.AlterField(
            model_name='player',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='housename',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='place',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='pname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='state',
            field=models.CharField(default=player.models.get_default_value, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='village',
            field=models.CharField(default=player.models.get_default_value, max_length=50, null=True),
        ),
    ]

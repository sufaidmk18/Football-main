# Generated by Django 4.1.7 on 2023-04-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_remove_staff_panchayath_remove_staff_sname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='match_details',
            name='status',
            field=models.CharField(choices=[('win', 'win'), ('loss', 'loss'), ('draw', 'draw')], default='draw', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='performance',
            name='assists',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='performance',
            name='cleansheets',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='performance',
            name='goals',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='performance',
            name='red_cards',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='performance',
            name='total_matches',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='performance',
            name='yellow_cards',
            field=models.IntegerField(),
        ),
    ]

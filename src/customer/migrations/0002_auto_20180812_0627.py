# Generated by Django 2.1 on 2018-08-12 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='location_y',
            field=models.IntegerField(default=0),
        ),
    ]

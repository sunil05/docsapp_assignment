# Generated by Django 2.1 on 2018-08-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180811_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='rides',
            name='nearest_driver',
            field=models.CharField(default='[]', max_length=500),
        ),
    ]

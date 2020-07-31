# Generated by Django 3.0.8 on 2020-07-31 09:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0005_auto_20200731_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='actors',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
        migrations.AddField(
            model_name='directors',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
        migrations.AddField(
            model_name='movies',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='poster'),
        ),
        migrations.AlterField(
            model_name='actors',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2020, 7, 31, 9, 27, 6, 750330, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='directors',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2020, 7, 31, 9, 27, 6, 750330, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movies',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 7, 31, 9, 27, 6, 801892, tzinfo=utc)),
        ),
    ]

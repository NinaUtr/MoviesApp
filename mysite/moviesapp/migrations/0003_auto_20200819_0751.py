# Generated by Django 3.1 on 2020-08-19 07:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0002_auto_20200805_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2020, 8, 19, 7, 51, 18, 959784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='actors',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='actors',
            name='photo',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='directors',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2020, 8, 19, 7, 51, 18, 959784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='directors',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='directors',
            name='photo',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='actors',
            field=models.ManyToManyField(blank=True, null=True, to='moviesapp.Actors'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 19, 7, 51, 18, 962300, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movies',
            name='directors',
            field=models.ManyToManyField(blank=True, null=True, to='moviesapp.Directors'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]

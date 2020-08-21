# Generated by Django 3.1 on 2020-08-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('birthday', models.DateField(default='2000-01-01')),
                ('photo', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('birthday', models.DateField(default='2000-01-01')),
                ('photo', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('plot', models.TextField(max_length=1000, null=True)),
                ('date', models.DateField(default='2000-01-01')),
                ('poster', models.URLField(null=True)),
                ('actors', models.ManyToManyField(blank=True, to='moviesapp.Actors')),
                ('directors', models.ManyToManyField(blank=True, to='moviesapp.Directors')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testo_footer', models.TextField(blank=True)),
                ('immagine_box_1', models.FileField(blank=True, max_length=500, upload_to='home/img/')),
                ('immagine_box_2', models.FileField(blank=True, max_length=500, upload_to='home/img/')),
                ('immagine_box_3', models.FileField(blank=True, max_length=500, upload_to='home/img/')),
                ('immagine_box_4', models.FileField(blank=True, max_length=500, upload_to='home/img/')),
                ('cambia_automaticamente_gallery', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Modifica il contenuto della Home',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immagine', models.FileField(max_length=500, upload_to='home/slide/')),
                ('titolo', models.CharField(blank=True, max_length=100)),
                ('attivo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Modifica le immagini della Slide',
            },
        ),
        migrations.DeleteModel(
            name='Home',
        ),
    ]

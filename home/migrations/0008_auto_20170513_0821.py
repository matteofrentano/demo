# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170513_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenuto',
            name='testo_box_1',
            field=models.TextField(blank=True, max_length=3000),
        ),
        migrations.AddField(
            model_name='contenuto',
            name='testo_box_2',
            field=models.TextField(blank=True, max_length=3000),
        ),
        migrations.AddField(
            model_name='contenuto',
            name='testo_box_3',
            field=models.TextField(blank=True, max_length=3000),
        ),
        migrations.AddField(
            model_name='contenuto',
            name='testo_box_4',
            field=models.TextField(blank=True, max_length=3000),
        ),
    ]

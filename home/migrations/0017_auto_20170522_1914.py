# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20170522_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenuto',
            name='link_fb',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contenuto',
            name='link_gp',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contenuto',
            name='link_ig',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contenuto',
            name='link_lk',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contenuto',
            name='link_tw',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contenuto',
            name='link_yt',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
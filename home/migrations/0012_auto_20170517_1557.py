# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_work_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]

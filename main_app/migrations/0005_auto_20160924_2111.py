# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20160924_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneaker',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='sneaker_images'),
        ),
    ]

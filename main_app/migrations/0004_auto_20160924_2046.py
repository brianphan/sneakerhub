# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20160924_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneaker',
            name='image',
            field=models.ImageField(default='media2/default.png', upload_to='sneaker_images'),
        ),
    ]

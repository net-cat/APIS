# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-20 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_auto_20161020_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablesize',
            name='partnerMax',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tablesize',
            name='partnerMin',
            field=models.IntegerField(default=1),
        ),
    ]

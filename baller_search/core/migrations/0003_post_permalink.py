# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-22 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170522_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='permalink',
            field=models.CharField(default=None, max_length=255, verbose_name='Link where the post can be forever found'),
            preserve_default=False,
        ),
    ]

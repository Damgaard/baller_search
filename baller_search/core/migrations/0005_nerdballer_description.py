# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170523_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='nerdballer',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Why is this person a sick Nerd Baller?'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-11 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20160327_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='reset',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointments',
            name='restored',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

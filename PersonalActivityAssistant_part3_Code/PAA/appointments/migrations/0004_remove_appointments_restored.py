# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-11 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20160410_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='restored',
        ),
    ]
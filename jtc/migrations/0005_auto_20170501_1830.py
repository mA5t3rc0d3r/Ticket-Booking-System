# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtc', '0004_auto_20170501_0250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='time',
            options={'ordering': ['timing']},
        ),
        migrations.AlterUniqueTogether(
            name='multiplex',
            unique_together=set([]),
        ),
    ]

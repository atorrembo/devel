# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 02:28
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmo', '0007_auto_20161016_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='area',
            field=django.contrib.gis.db.models.fields.PolygonField(null=True, srid=4326),
        ),
    ]

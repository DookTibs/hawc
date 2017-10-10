# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-08 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0012_add_datapivot_barchart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapivot',
            name='caption',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='visual',
            name='caption',
            field=models.TextField(blank=True),
        ),
    ]
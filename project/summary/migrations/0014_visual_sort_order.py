# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-12 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0013_auto_20170806_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='visual',
            name='sort_order',
            field=models.CharField(choices=[('short_citation', 'Short Citation'), ('overall_confidence', 'Final Study Confidence')], default='short_citation', max_length=40),
        ),
    ]
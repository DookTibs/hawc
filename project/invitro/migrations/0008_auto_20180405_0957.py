# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-05 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitro', '0007_auto_20170806_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ivendpoint',
            name='LOEL',
            field=models.SmallIntegerField(default=-999, help_text='Lowest observed adverse effect level', verbose_name='LOAEL'),
        ),
        migrations.AlterField(
            model_name='ivendpoint',
            name='NOEL',
            field=models.SmallIntegerField(default=-999, help_text='No observed adverse effect level', verbose_name='NOAEL'),
        ),
    ]

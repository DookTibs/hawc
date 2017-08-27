# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-26 23:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riskofbias', '0015_auto_20170809_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskOfBiasScoreChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_number', models.PositiveSmallIntegerField(choices=[(10, 'Not reported'), (1, 'Critically deficient'), (2, 'Poor'), (3, 'Adequate'), (4, 'Good'), (0, 'Not applicable')], default=10)),
                ('score_name', models.CharField(max_length=50)),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scorechoices', to='riskofbias.RiskOfBiasMetric')),
            ],
        ),
    ]
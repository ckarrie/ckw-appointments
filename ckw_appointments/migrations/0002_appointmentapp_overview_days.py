# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-18 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckw_appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentapp',
            name='overview_days',
            field=models.PositiveIntegerField(default=7),
        ),
    ]

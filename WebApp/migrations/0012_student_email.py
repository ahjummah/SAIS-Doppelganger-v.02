# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0011_auto_20160527_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0012_auto_20170602_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstories',
            name='tool_tip',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-16 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_add_category_order_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='report_reason',
            field=models.TextField(blank=True, default=b'', verbose_name='report_reason'),
        ),
    ]
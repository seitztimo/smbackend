# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-04 09:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0053_department_municipality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='origin_last_modified_time',
            new_name='last_modified_time',
        ),
    ]

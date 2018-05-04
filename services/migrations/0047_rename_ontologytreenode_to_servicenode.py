# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-05 13:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0046_remove_organization_model'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OntologyTreeNode',
            new_name='ServiceNode',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='root_ontologytreenodes',
            new_name='root_servicenodes',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='service_tree_nodes',
            new_name='service_nodes',
        ),
    ]
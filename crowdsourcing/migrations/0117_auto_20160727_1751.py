# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-27 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0116_auto_20160726_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='has_peer_review',
            new_name='is_reviewed',
        ),
    ]
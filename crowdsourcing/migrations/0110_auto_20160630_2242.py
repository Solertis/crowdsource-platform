# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-30 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0109_auto_20160630_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialaccount',
            name='type',
            field=models.IntegerField(choices=[(1, b'Earnings'), (2, b'Deposits'), (3, b'Escrow')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=19, null=True),
        ),
    ]

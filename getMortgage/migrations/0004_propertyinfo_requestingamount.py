# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getMortgage', '0003_propertyinfo_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyinfo',
            name='requestingAmount',
            field=models.IntegerField(default=250000),
            preserve_default=False,
        ),
    ]
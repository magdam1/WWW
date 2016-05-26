# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obwody', '0006_auto_20150424_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gmina_miasto',
            name='nazwa',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='obwod',
            name='nazwa',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='powiat_miasto',
            name='nazwa',
            field=models.CharField(max_length=500),
        ),
    ]

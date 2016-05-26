# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obwody', '0005_auto_20150423_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powiat_miasto',
            name='ma_gminy',
            field=models.IntegerField(default=0),
        ),
    ]

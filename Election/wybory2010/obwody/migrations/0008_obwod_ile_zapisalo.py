# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obwody', '0007_auto_20150424_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='obwod',
            name='ile_zapisalo',
            field=models.IntegerField(default=0),
        ),
    ]

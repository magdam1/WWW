# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obwody', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obwod',
            name='upr_do_glos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='obwod',
            name='wydano_kart',
            field=models.IntegerField(default=0),
        ),
    ]

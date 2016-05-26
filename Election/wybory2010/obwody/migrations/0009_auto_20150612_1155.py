# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obwody', '0008_obwod_ile_zapisalo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obwod',
            name='ile_zapisalo',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='obwod',
            name='uprawnionych_do_glosowania',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='obwod',
            name='wydano_kart',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

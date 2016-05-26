# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obwody', '0002_auto_20150422_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gmina',
            name='miasto',
            field=models.ForeignKey(blank=True, to='obwody.Miasto', null=True),
        ),
        migrations.AlterField(
            model_name='gmina',
            name='powiat',
            field=models.ForeignKey(blank=True, to='obwody.Powiat', null=True),
        ),
        migrations.AlterField(
            model_name='miasto',
            name='powiat',
            field=models.ForeignKey(blank=True, to='obwody.Powiat', null=True),
        ),
        migrations.AlterField(
            model_name='miasto',
            name='wojewodztwo',
            field=models.ForeignKey(blank=True, to='obwody.Wojewodztwo', null=True),
        ),
        migrations.AlterField(
            model_name='obwod',
            name='gmina',
            field=models.ForeignKey(blank=True, to='obwody.Gmina', null=True),
        ),
        migrations.AlterField(
            model_name='obwod',
            name='miasto',
            field=models.ForeignKey(blank=True, to='obwody.Miasto', null=True),
        ),
    ]

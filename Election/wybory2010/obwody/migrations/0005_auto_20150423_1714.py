# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obwody', '0004_auto_20150422_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gmina_Miasto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Powiat_Miasto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=100)),
                ('ma_gminy', models.IntegerField(default=1)),
                ('wojewodztwo', models.ForeignKey(to='obwody.Wojewodztwo')),
            ],
        ),
        migrations.RemoveField(
            model_name='gmina',
            name='miasto',
        ),
        migrations.RemoveField(
            model_name='gmina',
            name='powiat',
        ),
        migrations.RemoveField(
            model_name='miasto',
            name='powiat',
        ),
        migrations.RemoveField(
            model_name='miasto',
            name='wojewodztwo',
        ),
        migrations.RemoveField(
            model_name='powiat',
            name='wojewodztwo',
        ),
        migrations.AlterField(
            model_name='obwod',
            name='gmina',
            field=models.ForeignKey(blank=True, to='obwody.Gmina_Miasto', null=True),
        ),
        migrations.AlterField(
            model_name='obwod',
            name='miasto',
            field=models.ForeignKey(blank=True, to='obwody.Powiat_Miasto', null=True),
        ),
        migrations.DeleteModel(
            name='Gmina',
        ),
        migrations.DeleteModel(
            name='Miasto',
        ),
        migrations.DeleteModel(
            name='Powiat',
        ),
        migrations.AddField(
            model_name='gmina_miasto',
            name='powiat',
            field=models.ForeignKey(to='obwody.Powiat_Miasto'),
        ),
    ]

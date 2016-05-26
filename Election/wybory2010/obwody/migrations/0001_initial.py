# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gmina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Miasto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Obwod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=200)),
                ('gmina', models.ForeignKey(to='obwody.Gmina', null=True)),
                ('miasto', models.ForeignKey(to='obwody.Miasto', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Powiat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wojewodztwo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='powiat',
            name='wojewodztwo',
            field=models.ForeignKey(to='obwody.Wojewodztwo'),
        ),
        migrations.AddField(
            model_name='miasto',
            name='powiat',
            field=models.ForeignKey(to='obwody.Powiat', null=True),
        ),
        migrations.AddField(
            model_name='miasto',
            name='wojewodztwo',
            field=models.ForeignKey(to='obwody.Wojewodztwo', null=True),
        ),
        migrations.AddField(
            model_name='gmina',
            name='miasto',
            field=models.ForeignKey(to='obwody.Miasto', null=True),
        ),
        migrations.AddField(
            model_name='gmina',
            name='powiat',
            field=models.ForeignKey(to='obwody.Powiat', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obwody', '0003_auto_20150422_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obwod',
            old_name='upr_do_glos',
            new_name='uprawnionych_do_glosowania',
        ),
    ]

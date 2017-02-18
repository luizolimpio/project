# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170206_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='cidade',
            name='ativo',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

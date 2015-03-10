# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='status',
            field=models.BooleanField(default=False, verbose_name='status'),
            preserve_default=True,
        ),
    ]

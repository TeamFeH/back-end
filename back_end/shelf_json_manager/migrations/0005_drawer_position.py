# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf_json_manager', '0004_auto_20150210_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawer',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

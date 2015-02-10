# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf_json_manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdf',
            old_name='name',
            new_name='pdf_name',
        ),
    ]

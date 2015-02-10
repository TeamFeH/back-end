# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shelf_json_manager', '0002_auto_20150210_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='pdf_file',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'pdf_files'),
            preserve_default=True,
        ),
    ]

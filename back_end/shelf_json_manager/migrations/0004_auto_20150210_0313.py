# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf_json_manager', '0003_auto_20150210_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='pdf_file',
            field=models.FileField(upload_to=b'pdf_files'),
            preserve_default=True,
        ),
    ]

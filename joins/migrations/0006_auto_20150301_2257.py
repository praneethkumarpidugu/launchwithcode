# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0005_auto_20150301_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.CharField(max_length=120, unique=True, default='ABC'),
            preserve_default=True,
        ),
    ]

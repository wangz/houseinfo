# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170327_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='msummary',
            name='city',
            field=models.CharField(default='bj', max_length=20, choices=[(b'bj', b'BeiJing'), (b'sh', b'ShangHai')]),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_data_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='city',
            field=models.CharField(max_length=20, choices=[(b'bj', b'BeiJing'), (b'sh', b'ShangHai')]),
        ),
    ]

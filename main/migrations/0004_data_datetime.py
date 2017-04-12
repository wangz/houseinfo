# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='datetime',
            field=models.DateField(default=datetime.datetime(2017, 3, 22, 3, 19, 5, 968076, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

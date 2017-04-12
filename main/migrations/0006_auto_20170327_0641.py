# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170322_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='desc1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='vtype',
            field=models.CharField(max_length=20, choices=[(b'r', b'\xe6\x88\xbf\xe6\xba\x90\xe6\x95\xb0'), (b'd', b'deal'), (b's', b'see'), (b'nc', b'\xe6\x96\xb0\xe5\xa2\x9e\xe5\xae\xa2\xe6\xba\x90'), (b'nh', b'\xe6\x96\xb0\xe5\xa2\x9e\xe6\x88\xbf\xe6\xba\x90'), (b'ns', b'\xe5\xb8\xa6\xe7\x9c\x8b\xe9\x87\x8f'), (b'td', b'\xe5\x8e\x86\xe5\x8f\xb2\xe6\x80\xbb\xe6\x88\x90\xe4\xba\xa4')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170327_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='MSummary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=500, null=True)),
                ('datetime', models.DateField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='data',
            name='vtype',
            field=models.CharField(max_length=20, choices=[(b'r', b'\xe6\x88\xbf\xe6\xba\x90\xe6\x95\xb0'), (b'd', b'deal'), (b'nc', b'\xe6\x96\xb0\xe5\xa2\x9e\xe5\xae\xa2\xe6\xba\x90'), (b'nh', b'\xe6\x96\xb0\xe5\xa2\x9e\xe6\x88\xbf\xe6\xba\x90'), (b'ns', b'\xe5\xb8\xa6\xe7\x9c\x8b\xe9\x87\x8f'), (b'mnc', b'\xe6\x9c\x88\xe6\x96\xb0\xe5\xa2\x9e\xe5\xae\xa2\xe6\xba\x90'), (b'mnh', b'\xe6\x9c\x88\xe6\x96\xb0\xe5\xa2\x9e\xe6\x88\xbf\xe6\xba\x90'), (b'mns', b'\xe6\x9c\x88\xe5\xb8\xa6\xe7\x9c\x8b\xe9\x87\x8f'), (b'td', b'\xe5\x8e\x86\xe5\x8f\xb2\xe6\x80\xbb\xe6\x88\x90\xe4\xba\xa4')]),
        ),
    ]

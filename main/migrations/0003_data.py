# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170321_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=20)),
                ('vtype', models.CharField(max_length=20, choices=[(b'r', b'residual'), (b'd', b'deal'), (b's', b'see'), (b'nc', b'newcustomer'), (b'nh', b'newhouse')])),
                ('value', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

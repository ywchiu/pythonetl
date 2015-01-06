# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0002_join_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default=b'ABC', unique=True, max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='join',
            unique_together=set([('email', 'ref_id')]),
        ),
    ]

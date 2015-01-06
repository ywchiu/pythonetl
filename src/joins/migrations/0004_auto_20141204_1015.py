# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_auto_20141204_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='friend',
            field=models.ForeignKey(related_name='referral', blank=True, to='joins.Join', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skyend_configs', '0003_unidadmedida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidadmedida',
            name='test_image',
        ),
    ]

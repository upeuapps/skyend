# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skyend_configs', '0002_naturalperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(blank=True, null=True, max_length=10)),
                ('nombre', models.CharField(max_length=60)),
                ('estado', models.BooleanField(default=True)),
                ('test_date', models.DateTimeField(blank=True, null=True)),
                ('test_number', models.FloatField(blank=True, null=True)),
                ('test_image', models.ImageField(default='test_images/default.png', blank=True, null=True, upload_to='test_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'UnidadMedida',
                'verbose_name_plural': 'UnidadMedidas',
            },
        ),
    ]

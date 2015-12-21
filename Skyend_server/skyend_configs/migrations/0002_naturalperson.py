# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skyend_configs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaturalPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('last_name', models.CharField(max_length=10, null=True, blank=True)),
                ('first_name', models.TextField(max_length=60)),
                ('birth_date', models.DateTimeField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'NaturalPerson',
                'verbose_name_plural': 'NaturalPersons',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skyend_configs', '0005_insumo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('codigo', models.CharField(blank=True, null=True, max_length=10)),
                ('nombre', models.CharField(max_length=60)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.AddField(
            model_name='insumo',
            name='estado',
            field=models.CharField(choices=[('PRO', 'Activo'), ('WEB', 'Baja'), ('VENTAS', 'Otro')], default='PRO', max_length=50),
        ),
        migrations.AddField(
            model_name='insumo',
            name='categoria',
            field=models.ManyToManyField(blank=True, to='skyend_configs.Categoria', null=True, related_name='insumo_set'),
        ),
    ]

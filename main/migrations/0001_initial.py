# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangoyearlessdate.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YearlessDateModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yearless_date', djangoyearlessdate.models.YearlessDateField(max_length=4)),
                ('optional_yearless_date', djangoyearlessdate.models.YearlessDateField(max_length=4, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='YearModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', djangoyearlessdate.models.YearField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

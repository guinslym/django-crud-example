# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-01 16:19
from __future__ import unicode_literals

import applications.cardealer.models
import applications.music.models_utils
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', applications.music.models_utils.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', applications.music.models_utils.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('car_name', models.CharField(max_length=30)),
                ('car_model', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to=applications.cardealer.models.upload_to)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]

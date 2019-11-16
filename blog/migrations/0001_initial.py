# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-17 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.CharField(blank=True, help_text='simple description', max_length=100, verbose_name='Description')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_contents', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

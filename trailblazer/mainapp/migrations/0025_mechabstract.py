# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2023-04-21 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_civilabstract'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mechabstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Email', models.EmailField(default='', max_length=50)),
                ('Project', models.CharField(default='', max_length=50)),
                ('Abstract', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2023-04-16 11:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='FeedBack',
        ),
    ]

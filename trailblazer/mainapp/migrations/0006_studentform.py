# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2023-03-24 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Enter first name')),
                ('lastname', models.CharField(max_length=50, verbose_name='Enter last name')),
                ('email', models.EmailField(max_length=254, verbose_name='Enter Email')),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]

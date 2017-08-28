# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 15:57
from __future__ import unicode_literals

import AutoGrade.models
import AutoGrade.storage
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('AutoGrade', '0012_auto_20170828_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='assignment_file',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='config_file',
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignment_files',
            field=filer.fields.file.FilerFileField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='filer_assignment_files', to='filer.File'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='instructor_test',
            field=models.FileField(default=None, storage=AutoGrade.storage.OverwriteStorage(), upload_to=AutoGrade.models.assignment_directory_path),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='student_test',
            field=models.FileField(default=None, storage=AutoGrade.storage.OverwriteStorage(), upload_to=AutoGrade.models.assignment_directory_path),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('email_Spam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email_new',
            name='email_filtered',
        ),
        migrations.AddField(
            model_name='email_new',
            name='email_new',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='email_Spam.Email'),
            preserve_default=False,
        ),
    ]
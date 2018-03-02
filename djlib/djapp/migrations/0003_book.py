# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-01 15:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0002_auto_20180301_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('edition', models.CharField(max_length=5)),
                ('publisher', models.CharField(max_length=20)),
                ('issue_date', models.DateField()),
                ('book_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
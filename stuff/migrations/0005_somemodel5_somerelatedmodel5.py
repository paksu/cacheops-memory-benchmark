# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0004_somemodel4_somerelatedmodel4'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel5',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SomeRelatedModel5',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('f1', models.CharField(max_length=200)),
                ('f2', models.CharField(max_length=200)),
                ('f3', models.CharField(max_length=200)),
                ('f4', models.CharField(max_length=200)),
                ('f5', models.CharField(max_length=200)),
                ('f6', models.CharField(max_length=200)),
                ('counter', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='stuff.SomeModel5')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(unique=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('some_boolean1', models.BooleanField(default=True)),
                ('some_boolean2', models.BooleanField(default=True)),
                ('some_boolean3', models.BooleanField(default=True)),
                ('some_boolean4', models.BooleanField(default=True)),
                ('some_boolean5', models.BooleanField(default=True)),
                ('some_boolean6', models.BooleanField(default=True)),
                ('some_boolean7', models.BooleanField(default=True)),
                ('some_boolean8', models.BooleanField(default=True)),
                ('some_boolean9', models.BooleanField(default=True)),
                ('some_boolean10', models.BooleanField(default=True)),
                ('some_msg1', models.CharField(max_length=1024, null=True, blank=True)),
                ('some_msg2', models.CharField(max_length=1024, null=True, blank=True)),
                ('some_msg3', models.CharField(max_length=1024, null=True, blank=True)),
                ('some_msg4', models.CharField(max_length=1024, null=True, blank=True)),
                ('some_msg5', models.CharField(max_length=1024, null=True, blank=True)),
                ('some_msg6', models.CharField(max_length=1024, null=True, blank=True)),
                ('some_msg7', models.CharField(max_length=1024, null=True, blank=True)),
                ('some_msg8', models.CharField(max_length=1024, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(unique=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('is_something', models.BooleanField(default=True)),
                ('language_code', models.CharField(default=b'en', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestModel2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(unique=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('is_something', models.BooleanField(default=True)),
                ('language_code', models.CharField(default=b'en', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bigmodel',
            name='testmodel2',
            field=models.ForeignKey(related_name='more_test_models', verbose_name=b'TestModel2', to='morestuff.TestModel2', null=True),
        ),
        migrations.AddField(
            model_name='bigmodel',
            name='testmodel',
            field=models.ForeignKey(related_name='testmodels', verbose_name=b'TestModel', to='morestuff.TestModel'),
        ),
    ]

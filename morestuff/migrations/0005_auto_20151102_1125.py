# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morestuff', '0004_bazmodel_bazmodel2_bigmodel4'),
    ]

    operations = [
        migrations.CreateModel(
            name='aBigModel',
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
            name='aBigModel2',
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
            name='aBigModel3',
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
            name='aBigModel4',
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
        migrations.RenameModel(
            old_name='BarModel',
            new_name='aBarModel',
        ),
        migrations.RenameModel(
            old_name='TestModel2',
            new_name='aBarModel2',
        ),
        migrations.RenameModel(
            old_name='TestModel',
            new_name='aBazModel',
        ),
        migrations.RenameModel(
            old_name='FooModel',
            new_name='aBazModel2',
        ),
        migrations.RenameModel(
            old_name='FooModel2',
            new_name='aFooModel',
        ),
        migrations.RenameModel(
            old_name='BazModel',
            new_name='aFooModel2',
        ),
        migrations.RenameModel(
            old_name='BazModel2',
            new_name='aTestModel',
        ),
        migrations.RenameModel(
            old_name='BarModel2',
            new_name='aTestModel2',
        ),
        migrations.RemoveField(
            model_name='bigmodel',
            name='testmodel',
        ),
        migrations.RemoveField(
            model_name='bigmodel',
            name='testmodel2',
        ),
        migrations.RemoveField(
            model_name='bigmodel2',
            name='foomodel',
        ),
        migrations.RemoveField(
            model_name='bigmodel2',
            name='foomodel2',
        ),
        migrations.RemoveField(
            model_name='bigmodel3',
            name='barmodel',
        ),
        migrations.RemoveField(
            model_name='bigmodel3',
            name='barmodel2',
        ),
        migrations.RemoveField(
            model_name='bigmodel4',
            name='bazmodel',
        ),
        migrations.RemoveField(
            model_name='bigmodel4',
            name='bazmodel2',
        ),
        migrations.DeleteModel(
            name='BigModel',
        ),
        migrations.DeleteModel(
            name='BigModel2',
        ),
        migrations.DeleteModel(
            name='BigModel3',
        ),
        migrations.DeleteModel(
            name='BigModel4',
        ),
        migrations.AddField(
            model_name='abigmodel4',
            name='bazmodel',
            field=models.ForeignKey(related_name='testmodels', verbose_name=b'BazModel', to='morestuff.aBazModel'),
        ),
        migrations.AddField(
            model_name='abigmodel4',
            name='bazmodel2',
            field=models.ForeignKey(related_name='more_test_models', verbose_name=b'BazModel2', to='morestuff.aBazModel2', null=True),
        ),
        migrations.AddField(
            model_name='abigmodel3',
            name='barmodel',
            field=models.ForeignKey(related_name='testmodels', verbose_name=b'BarModel', to='morestuff.aBarModel'),
        ),
        migrations.AddField(
            model_name='abigmodel3',
            name='barmodel2',
            field=models.ForeignKey(related_name='more_test_models', verbose_name=b'BarModel2', to='morestuff.aBarModel2', null=True),
        ),
        migrations.AddField(
            model_name='abigmodel2',
            name='foomodel',
            field=models.ForeignKey(related_name='testmodels', verbose_name=b'FooModel', to='morestuff.aFooModel'),
        ),
        migrations.AddField(
            model_name='abigmodel2',
            name='foomodel2',
            field=models.ForeignKey(related_name='more_test_models', verbose_name=b'FooModel2', to='morestuff.aFooModel2', null=True),
        ),
        migrations.AddField(
            model_name='abigmodel',
            name='testmodel',
            field=models.ForeignKey(related_name='testmodels', verbose_name=b'TestModel', to='morestuff.aTestModel'),
        ),
        migrations.AddField(
            model_name='abigmodel',
            name='testmodel2',
            field=models.ForeignKey(related_name='more_test_models', verbose_name=b'TestModel2', to='morestuff.aTestModel2', null=True),
        ),
    ]

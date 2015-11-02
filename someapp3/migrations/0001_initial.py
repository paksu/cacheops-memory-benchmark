# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SomeAnotherRelatedModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('f1', models.CharField(max_length=200)),
                ('f2', models.CharField(max_length=200)),
                ('f3', models.CharField(max_length=200)),
                ('f4', models.CharField(max_length=200)),
                ('f5', models.CharField(max_length=200)),
                ('f6', models.CharField(max_length=200)),
                ('f7', models.CharField(max_length=200, null=True, blank=True)),
                ('f8', models.CharField(max_length=200, null=True, blank=True)),
                ('counter', models.IntegerField(default=0)),
                ('counter2', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SomeAnotherRelatedModel2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('f1', models.CharField(max_length=200)),
                ('f2', models.CharField(max_length=200)),
                ('f3', models.CharField(max_length=200)),
                ('f4', models.CharField(max_length=200)),
                ('f5', models.CharField(max_length=200)),
                ('f6', models.CharField(max_length=200)),
                ('f7', models.CharField(max_length=200, null=True, blank=True)),
                ('f8', models.CharField(max_length=200, null=True, blank=True)),
                ('counter', models.IntegerField(default=0)),
                ('counter2', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SomeModel2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SomeModel3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SomeModel4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SomeModel5',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SomeRelatedModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('f1', models.CharField(max_length=200)),
                ('f2', models.CharField(max_length=200)),
                ('f3', models.CharField(max_length=200)),
                ('f4', models.CharField(max_length=200)),
                ('f5', models.CharField(max_length=200)),
                ('f6', models.CharField(max_length=200)),
                ('f7', models.CharField(max_length=200, null=True, blank=True)),
                ('f8', models.CharField(max_length=200, null=True, blank=True)),
                ('counter', models.IntegerField(default=0)),
                ('counter2', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='someapp3.SomeModel')),
            ],
        ),
        migrations.CreateModel(
            name='SomeRelatedModel2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('f1', models.CharField(max_length=200)),
                ('f2', models.CharField(max_length=200)),
                ('f3', models.CharField(max_length=200)),
                ('f4', models.CharField(max_length=200)),
                ('f5', models.CharField(max_length=200)),
                ('f6', models.CharField(max_length=200)),
                ('f7', models.CharField(max_length=200, null=True, blank=True)),
                ('f8', models.CharField(max_length=200, null=True, blank=True)),
                ('counter', models.IntegerField(default=0)),
                ('counter2', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='someapp3.SomeModel2')),
            ],
        ),
        migrations.CreateModel(
            name='SomeRelatedModel3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('f1', models.CharField(max_length=200)),
                ('f2', models.CharField(max_length=200)),
                ('f3', models.CharField(max_length=200)),
                ('f4', models.CharField(max_length=200)),
                ('f5', models.CharField(max_length=200)),
                ('f6', models.CharField(max_length=200)),
                ('f7', models.CharField(max_length=200, null=True, blank=True)),
                ('f8', models.CharField(max_length=200, null=True, blank=True)),
                ('counter', models.IntegerField(default=0)),
                ('counter2', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='someapp3.SomeModel3')),
            ],
        ),
        migrations.CreateModel(
            name='SomeRelatedModel4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('f1', models.CharField(max_length=200)),
                ('f2', models.CharField(max_length=200)),
                ('f3', models.CharField(max_length=200)),
                ('f4', models.CharField(max_length=200)),
                ('f5', models.CharField(max_length=200)),
                ('f6', models.CharField(max_length=200)),
                ('f7', models.CharField(max_length=200, null=True, blank=True)),
                ('f8', models.CharField(max_length=200, null=True, blank=True)),
                ('counter', models.IntegerField(default=0)),
                ('counter2', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='someapp3.SomeModel4')),
            ],
        ),
        migrations.CreateModel(
            name='SomeRelatedModel5',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('f1', models.CharField(max_length=200)),
                ('f2', models.CharField(max_length=200)),
                ('f3', models.CharField(max_length=200)),
                ('f4', models.CharField(max_length=200)),
                ('f5', models.CharField(max_length=200)),
                ('f6', models.CharField(max_length=200)),
                ('f7', models.CharField(max_length=200, null=True, blank=True)),
                ('f8', models.CharField(max_length=200, null=True, blank=True)),
                ('counter', models.IntegerField(default=0)),
                ('counter2', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='someapp3.SomeModel5')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='somemodel5',
            unique_together=set([('content', 'uuid')]),
        ),
        migrations.AlterUniqueTogether(
            name='somemodel4',
            unique_together=set([('content', 'uuid')]),
        ),
        migrations.AlterUniqueTogether(
            name='somemodel3',
            unique_together=set([('content', 'uuid')]),
        ),
        migrations.AlterUniqueTogether(
            name='somemodel2',
            unique_together=set([('content', 'uuid')]),
        ),
        migrations.AlterUniqueTogether(
            name='somemodel',
            unique_together=set([('uuid', 'content')]),
        ),
        migrations.AddField(
            model_name='someanotherrelatedmodel2',
            name='question',
            field=models.ForeignKey(to='someapp3.SomeModel'),
        ),
        migrations.AddField(
            model_name='someanotherrelatedmodel',
            name='question',
            field=models.ForeignKey(to='someapp3.SomeModel'),
        ),
        migrations.AlterUniqueTogether(
            name='somerelatedmodel5',
            unique_together=set([('f1', 'f2')]),
        ),
        migrations.AlterUniqueTogether(
            name='somerelatedmodel4',
            unique_together=set([('f1', 'f2')]),
        ),
        migrations.AlterUniqueTogether(
            name='somerelatedmodel3',
            unique_together=set([('f1', 'f2')]),
        ),
        migrations.AlterUniqueTogether(
            name='somerelatedmodel2',
            unique_together=set([('f1', 'f2')]),
        ),
        migrations.AlterUniqueTogether(
            name='somerelatedmodel',
            unique_together=set([('f1', 'question')]),
        ),
        migrations.AlterUniqueTogether(
            name='someanotherrelatedmodel2',
            unique_together=set([('f1', 'f2')]),
        ),
        migrations.AlterUniqueTogether(
            name='someanotherrelatedmodel',
            unique_together=set([('f1', 'question')]),
        ),
    ]

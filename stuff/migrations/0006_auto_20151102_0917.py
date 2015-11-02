# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0005_somemodel5_somerelatedmodel5'),
    ]

    operations = [
        migrations.AddField(
            model_name='someanotherrelatedmodel',
            name='counter2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='someanotherrelatedmodel',
            name='f7',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='someanotherrelatedmodel',
            name='f8',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='someanotherrelatedmodel2',
            name='counter2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='someanotherrelatedmodel2',
            name='f7',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='someanotherrelatedmodel2',
            name='f8',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='somerelatedmodel',
            name='counter2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='somerelatedmodel',
            name='f7',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='somerelatedmodel',
            name='f8',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='somerelatedmodel2',
            name='counter2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='somerelatedmodel2',
            name='f7',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='somerelatedmodel2',
            name='f8',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='somerelatedmodel3',
            name='counter2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='somerelatedmodel3',
            name='f7',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='somerelatedmodel3',
            name='f8',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='somerelatedmodel4',
            name='counter2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='somerelatedmodel4',
            name='f7',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='somerelatedmodel4',
            name='f8',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='somerelatedmodel5',
            name='counter2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='somerelatedmodel5',
            name='f7',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='somerelatedmodel5',
            name='f8',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]

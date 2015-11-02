# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0007_auto_20151102_0920'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='someanotherrelatedmodel',
            unique_together=set([('f1', 'question')]),
        ),
        migrations.AlterUniqueTogether(
            name='someanotherrelatedmodel2',
            unique_together=set([('f1', 'f2')]),
        ),
        migrations.AlterUniqueTogether(
            name='somemodel',
            unique_together=set([('uuid', 'content')]),
        ),
        migrations.AlterUniqueTogether(
            name='somemodel2',
            unique_together=set([('content', 'uuid')]),
        ),
        migrations.AlterUniqueTogether(
            name='somemodel3',
            unique_together=set([('content', 'uuid')]),
        ),
        migrations.AlterUniqueTogether(
            name='somemodel4',
            unique_together=set([('content', 'uuid')]),
        ),
        migrations.AlterUniqueTogether(
            name='somemodel5',
            unique_together=set([('content', 'uuid')]),
        ),
        migrations.AlterUniqueTogether(
            name='somerelatedmodel',
            unique_together=set([('f1', 'question')]),
        ),
        migrations.AlterUniqueTogether(
            name='somerelatedmodel2',
            unique_together=set([('f1', 'f2')]),
        ),
        migrations.AlterUniqueTogether(
            name='somerelatedmodel3',
            unique_together=set([('f1', 'f2')]),
        ),
        migrations.AlterUniqueTogether(
            name='somerelatedmodel4',
            unique_together=set([('f1', 'f2')]),
        ),
        migrations.AlterUniqueTogether(
            name='somerelatedmodel5',
            unique_together=set([('f1', 'f2')]),
        ),
    ]

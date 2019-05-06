# Generated by Django 2.0.6 on 2018-10-22 05:20
from __future__ import absolute_import, unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        # depends on higher numbers due to a squashed migration
        # that was later removed due to migration issues it caused
        ('django_celery_beat', '0005_add_solarschedule_events_choices'),
        ('django_celery_beat', '0006_auto_20180210_1226'),
        ('django_celery_beat', '0006_auto_20180322_0932'),
        ('django_celery_beat', '0007_auto_20180521_0826'),
        ('django_celery_beat', '0008_auto_20180914_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodictask',
            name='priority',
            field=models.PositiveIntegerField(
                blank=True,
                default=None,
                null=True,
                validators=[django.core.validators.MaxValueValidator(255)],
                verbose_name='priority'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=8)),
                ('image', models.ImageField(upload_to='equipment')),
                ('contact_number', models.TextField(max_length=15, null=True)),
                ('retrieved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New page', max_length=8, verbose_name='\u6807\u9898')),
                ('url', models.CharField(blank=True, max_length=4096, null=True, verbose_name='\u6307\u5411\u94fe\u63a5')),
                ('show_order', models.SmallIntegerField(default=0, verbose_name='\u5c55\u793a\u987a\u5e8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['show_order', '-create_time'],
                'verbose_name': '\u5bfc\u822a\u6761',
                'verbose_name_plural': '\u5bfc\u822a\u6761',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(auto_created=True, verbose_name='创建时间')),
                ('title', models.CharField(max_length=100, verbose_name='文章名称')),
                ('content', models.CharField(max_length=1000, verbose_name='文章内容')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '删除')], verbose_name='状态')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web1.Block', verbose_name='模块ID')),
            ],
            options={
                'verbose_name': '文章列表',
                'verbose_name_plural': '文章列表',
            },
        ),
    ]
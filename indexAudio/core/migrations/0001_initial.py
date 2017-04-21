# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.IntegerField(default=0, verbose_name='INDICE')),
                ('nome', models.CharField(max_length=200, verbose_name='NOME')),
                ('pub_date', models.DateTimeField(verbose_name='DATA CRIACAO')),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=200, verbose_name='EMPRESA')),
            ],
        ),
        migrations.AddField(
            model_name='audios',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresas'),
        ),
    ]

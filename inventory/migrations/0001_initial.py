# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-13 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('catalog', models.CharField(blank=True, max_length=45, null=True, verbose_name='Catalog number')),
                ('size', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Size of unit')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('comments', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(blank=True, max_length=64, null=True)),
                ('lookup_url', models.CharField(blank=True, help_text='url pattern to look up catalog number', max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
                ('rep', models.CharField(blank=True, max_length=45, null=True)),
                ('rep_phone', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Vendor'),
        ),
    ]
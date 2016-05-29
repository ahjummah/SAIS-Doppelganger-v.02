# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_auto_20160524_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, max_length=10, null=True)),
                ('time', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(blank=True, max_length=20, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(blank=True, max_length=20, null=True)),
                ('cluster_code', models.CharField(blank=True, max_length=20, null=True)),
                ('prof_id', models.CharField(blank=True, max_length=20, null=True)),
                ('schedule_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='year',
        ),
        migrations.AddField(
            model_name='school_info',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Student'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='schedule_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Subjects'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.School_Info'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 20:50
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('descripcion', models.CharField(blank=True, max_length=20, null=True)),
                ('banos', models.CharField(blank=True, max_length=5, null=True)),
                ('habitaciones', models.CharField(blank=True, max_length=5, null=True)),
                ('metros_terreno', models.CharField(blank=True, max_length=5, null=True)),
                ('metros_cubiertos', models.CharField(blank=True, max_length=5, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=150)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326, verbose_name='longitude/latitude')),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmo.Barrio')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmo.Ciudad')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('gis', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='inmueble',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmo.Pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmo.Pais'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmo.Ciudad'),
        ),
    ]

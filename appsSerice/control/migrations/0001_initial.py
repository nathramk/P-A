# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 10:16
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=50)),
                ('category_logo', models.FileField(upload_to='')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DetailOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_detailOrder', models.CharField(max_length=20)),
                ('cant_order', models.IntegerField()),
                ('subtotal_order', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('fecha_order', models.DateField(default=datetime.datetime(2017, 6, 30, 5, 16, 57, 533901))),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_order', models.CharField(max_length=20)),
                ('date_order', models.CharField(max_length=20)),
                ('status_order', models.BooleanField(default=False)),
                ('message_order', models.CharField(max_length=150)),
                ('code_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_person', models.CharField(max_length=30)),
                ('lastName_person', models.CharField(max_length=30)),
                ('doc_DNI', models.CharField(max_length=15)),
                ('country_person', models.CharField(max_length=15)),
                ('departament_person', models.CharField(max_length=20)),
                ('province_person', models.CharField(max_length=20)),
                ('district_person', models.CharField(max_length=20)),
                ('address_person', models.CharField(max_length=50)),
                ('phone_person', models.CharField(max_length=15)),
                ('mail_person', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_product', models.CharField(max_length=50)),
                ('nome_product', models.CharField(max_length=50)),
                ('marca_product', models.CharField(max_length=50)),
                ('cant_product', models.IntegerField()),
                ('precio_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('fecha_ingreso', models.DateField(default=datetime.datetime(2017, 6, 30, 5, 16, 57, 533901))),
                ('product_logo', models.FileField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Category')),
            ],
        ),
        migrations.AddField(
            model_name='detailorder',
            name='code_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Orders'),
        ),
        migrations.AddField(
            model_name='detailorder',
            name='code_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Product'),
        ),
        migrations.AddField(
            model_name='client',
            name='client_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Person'),
        ),
    ]

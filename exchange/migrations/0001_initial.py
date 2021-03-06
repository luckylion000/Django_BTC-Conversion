# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-29 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text=' code of crypto currency', max_length=3, unique=True)),
                ('name', models.CharField(help_text='name', max_length=200)),
                ('exchange_fee', models.FloatField(default=0.05)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Crypto Currency',
                'verbose_name_plural': 'Crypto Currencies',
            },
        ),
        migrations.CreateModel(
            name='IpTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('counter', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('payed_amount', models.FloatField(default=1)),
                ('received_amount', models.FloatField(default=1)),
                ('address', models.CharField(help_text='address', max_length=200)),
                ('address_id', models.CharField(help_text='address id', max_length=36)),
                ('batch', models.CharField(blank=True, help_text='BATCH ', max_length=200)),
                ('beneficiary_firstname', models.CharField(help_text='beneficiary first name ', max_length=200)),
                ('beneficiary_lastname', models.CharField(help_text='beneficiary last name ', max_length=200)),
                ('iban', models.CharField(help_text='iban ', max_length=200)),
                ('bic', models.CharField(help_text='bic ', max_length=200)),
                ('payment_purpose', models.CharField(help_text='payment purpose ', max_length=200)),
                ('country', models.CharField(default='', help_text='country', max_length=200)),
                ('email', models.CharField(default='', help_text='country', max_length=200)),
                ('received', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('sepa_executed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('crypto_currency', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='crypto_currency', to='exchange.CryptoCurrency')),
            ],
        ),
        migrations.CreateModel(
            name='SepaCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(help_text='country', max_length=200)),
                ('sepa_enable', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'SEPA Country',
                'verbose_name_plural': 'SEPA Countrys',
            },
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-02 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockClose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('timestamp', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StockDetails',
            fields=[
                ('symbol', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('currency', models.CharField(max_length=20)),
                ('instrument_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StockHigh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('timestamp', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StockLow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('timestamp', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StockOpen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('timestamp', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StockVolume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('timestamp', models.BigIntegerField(default=0)),
                ('value', models.FloatField(default=0, max_length=50)),
            ],
        ),
    ]

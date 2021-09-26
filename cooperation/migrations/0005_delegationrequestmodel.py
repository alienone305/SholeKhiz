# Generated by Django 3.2 on 2021-09-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperation', '0004_auto_20210926_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelegationRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('last_name', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('province', models.CharField(max_length=264)),
                ('city', models.CharField(max_length=264)),
                ('phone_number', models.IntegerField()),
                ('cellphone_number', models.IntegerField()),
                ('address', models.TextField()),
                ('area', models.IntegerField()),
                ('for_towerdryer', models.BooleanField(default=False)),
                ('for_package', models.BooleanField(default=False)),
                ('for_radiator', models.BooleanField(default=False)),
                ('for_waterheater', models.BooleanField(default=False)),
                ('has_reservoir', models.BooleanField(default=False)),
                ('fax_number', models.IntegerField(blank=True, null=True)),
                ('sell_prediction_towerdryer', models.IntegerField(blank=True, null=True)),
                ('sell_prediction_package', models.IntegerField(blank=True, null=True)),
                ('sell_prediction_radiator', models.IntegerField(blank=True, null=True)),
                ('sell_prediction_waterheater', models.IntegerField(blank=True, null=True)),
                ('attendance', models.CharField(blank=True, max_length=264, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('ownership_type', models.CharField(blank=True, max_length=264, null=True)),
            ],
        ),
    ]

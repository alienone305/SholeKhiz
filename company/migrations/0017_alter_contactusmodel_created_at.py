# Generated by Django 3.2 on 2021-10-13 11:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0016_alter_contactusmodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 11, 10, 46, 446875, tzinfo=utc)),
        ),
    ]
# Generated by Django 3.2 on 2021-09-28 10:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_alter_contactusmodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 10, 27, 57, 609690, tzinfo=utc)),
        ),
    ]

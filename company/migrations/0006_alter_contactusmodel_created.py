# Generated by Django 3.2 on 2021-09-25 09:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_contactusmodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 25, 9, 17, 42, 972411, tzinfo=utc)),
        ),
    ]

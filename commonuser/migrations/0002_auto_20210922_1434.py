# Generated by Django 3.2 on 2021-09-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commonusermodel',
            name='picture',
        ),
        migrations.AddField(
            model_name='commonusermodel',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]

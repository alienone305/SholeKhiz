# Generated by Django 3.2 on 2021-09-26 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperation', '0003_auto_20210926_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='descriprion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='resome',
            field=models.FileField(blank=True, null=True, upload_to='media/resome/'),
        ),
    ]

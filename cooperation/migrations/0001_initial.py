# Generated by Django 3.2 on 2021-09-25 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOpportunityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=264)),
                ('required_skills', models.TextField()),
                ('descriprion', models.TextField()),
            ],
        ),
    ]

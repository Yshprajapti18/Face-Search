# Generated by Django 5.0.6 on 2024-05-13 20:36

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_clientfaces_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=8)),
                ('pic', models.FileField(upload_to=api.models.upload_to_path_face)),
            ],
        ),
    ]
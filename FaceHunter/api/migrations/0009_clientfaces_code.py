# Generated by Django 5.0.6 on 2024-05-13 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_clientfaces_pic_alter_room_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientfaces',
            name='code',
            field=models.CharField(default='', max_length=8),
        ),
    ]

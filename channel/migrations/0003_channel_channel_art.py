# Generated by Django 5.0.7 on 2024-07-24 09:08

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_channel_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='channel_art',
            field=models.ImageField(blank=True, default='channel-art.jpg', null=True, upload_to=core.models.user_directory_path),
        ),
    ]

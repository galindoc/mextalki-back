# Generated by Django 3.2.7 on 2021-11-10 00:22

from django.db import migrations, models

import src.mextalki.models.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(
                blank=True, default=None, null=True,
                upload_to=src.mextalki.models.utils.upload_to_v2,
            ),
        ),
    ]

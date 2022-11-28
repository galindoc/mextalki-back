# Generated by Django 3.2.7 on 2021-10-27 22:19

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mextalki', '0042_auto_20211025_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadershipScore',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True, serialize=False, verbose_name='ID',
                    ),
                ),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'created_at', models.DateField(
                        blank=True, default=datetime.datetime(
                            2021, 10, 27, 22, 19, 45, 315511, tzinfo=utc,
                        ), null=True,
                    ),
                ),
                ('active', models.BooleanField(default=True)),
                ('exp_points', models.IntegerField(default=0)),
                (
                    'user', models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='leadership_board_score', to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'ordering': ('-exp_points',),
            },
        ),
    ]
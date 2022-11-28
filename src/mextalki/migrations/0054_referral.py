# Generated by Django 3.2.7 on 2022-01-30 19:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mextalki', '0053_video_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True, serialize=False, verbose_name='ID',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(blank=True, max_length=36, null=True)),
                ('purchased_plan', models.BooleanField(default=False)),
                (
                    'recommended_by', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='referrals', to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'user', models.OneToOneField(
                        blank=True, null=True,
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
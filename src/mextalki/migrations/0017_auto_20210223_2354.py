# Generated by Django 3.1.7 on 2021-02-24 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mextalki', '0016_auto_20210223_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheduledevent',
            old_name='provider_id',
            new_name='provider_event_id',
        ),
        migrations.AddField(
            model_name='scheduledevent',
            name='provider_invite_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='calendar_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='scheduledevent',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scheduledevent',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

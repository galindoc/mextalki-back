# Generated by Django 3.2.16 on 2022-10-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mextalki', '0069_auto_20221012_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='preview',
            field=models.TextField(),
        ),
    ]
# Generated by Django 3.2.11 on 2022-05-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0004_auto_20220501_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptiontype',
            name='billing_cycle',
            field=models.CharField(
                choices=[('MONTH', 'MONTHLY'), ('6 MONTHS', '6 MONTHS')], default='MONTH', max_length=10),
        ),
    ]

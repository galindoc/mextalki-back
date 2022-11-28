# Generated by Django 3.1.4 on 2020-12-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mextalki', '0005_stripepayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listeningpracticeaudio',
            name='transcription',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='stripepayment',
            name='billing_reason',
            field=models.CharField(
                choices=[
                    ('subscription_cycle', 'subscription cycle'), ('subscription_create', 'subscription create'), (
                        'subscription_update', 'subscription update',
                    ), ('subscription', 'subscription'), ('manual', 'manual'),
                ], max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name='stripepayment',
            name='charge_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stripepayment',
            name='currency',
            field=models.CharField(
                choices=[('USD', 'USD'), ('MXN', 'MXN')], max_length=3,
            ),
        ),
        migrations.AlterField(
            model_name='stripepayment',
            name='customer_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stripepayment',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stripepayment',
            name='payment_intent',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stripepayment',
            name='status',
            field=models.CharField(
                choices=[
                    ('draft', 'draft'), ('open', 'open'), (
                        'paid', 'paid',
                    ), ('uncollectible', 'uncollectible'), ('void', 'void'),
                ], max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(
                choices=[
                    ('CREATED', 'CREATED'), ('ACTIVE', 'ACTIVE'), (
                        'CANCELLED', 'CANCELLED',
                    ), ('EXPIRED', 'EXPIRED'),
                ], default='CREATED', max_length=24,
            ),
        ),
    ]

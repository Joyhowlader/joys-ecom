# Generated by Django 4.2.10 on 2024-03-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paypal_transaction_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

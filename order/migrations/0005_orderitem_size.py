# Generated by Django 4.2.10 on 2024-03-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]

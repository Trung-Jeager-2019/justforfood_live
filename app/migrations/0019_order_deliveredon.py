# Generated by Django 2.2.5 on 2019-10-07 17:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliveredOn',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

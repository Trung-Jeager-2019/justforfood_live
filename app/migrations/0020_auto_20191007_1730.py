# Generated by Django 2.2.5 on 2019-10-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_order_deliveredon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliveredOn',
            field=models.DateTimeField(blank=True),
        ),
    ]

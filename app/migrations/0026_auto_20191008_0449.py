# Generated by Django 2.2.5 on 2019-10-08 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20191008_0419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordereditem',
            old_name='orderId',
            new_name='order',
        ),
    ]

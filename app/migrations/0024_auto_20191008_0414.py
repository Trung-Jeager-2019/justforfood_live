# Generated by Django 2.2.5 on 2019-10-08 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20191008_0401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordereditems',
            old_name='OrderId',
            new_name='orderId',
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

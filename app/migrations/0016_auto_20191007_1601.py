# Generated by Django 2.2.5 on 2019-10-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20191006_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

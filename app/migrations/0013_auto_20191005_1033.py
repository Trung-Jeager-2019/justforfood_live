# Generated by Django 2.2.5 on 2019-10-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20191005_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

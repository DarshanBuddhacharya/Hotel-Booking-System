# Generated by Django 3.1.7 on 2021-05-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20210516_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancel',
            name='phnumber',
            field=models.BigIntegerField(max_length=12),
        ),
    ]

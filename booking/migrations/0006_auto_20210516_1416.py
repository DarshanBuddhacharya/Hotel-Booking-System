# Generated by Django 3.1.7 on 2021-05-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20210516_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phnumber',
            field=models.BigIntegerField(max_length=12),
        ),
    ]
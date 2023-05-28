# Generated by Django 4.1 on 2023-02-08 14:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_alter_auction_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='bid',
        ),
        migrations.AddField(
            model_name='bid',
            name='auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.auction'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 8, 15, 55, 41, 237343)),
        ),
    ]

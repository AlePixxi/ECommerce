# Generated by Django 4.1 on 2023-04-03 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_rename_initial_bid_auction_offert_remove_bid_auction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 4, 3, 10, 6, 30, 923601)),
        ),
    ]
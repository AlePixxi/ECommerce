# Generated by Django 4.1 on 2023-04-11 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_user_watchlist_alter_auction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 4, 11, 11, 15, 49, 965357)),
        ),
    ]

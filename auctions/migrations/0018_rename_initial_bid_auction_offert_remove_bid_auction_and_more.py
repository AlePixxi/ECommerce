# Generated by Django 4.1 on 2023-04-03 07:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auction_initial_bid_alter_auction_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='initial_bid',
            new_name='offert',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='auction',
        ),
        migrations.AddField(
            model_name='auction',
            name='bid',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 4, 3, 9, 57, 13, 311817)),
        ),
    ]

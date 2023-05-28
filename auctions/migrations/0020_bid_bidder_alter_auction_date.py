# Generated by Django 4.1 on 2023-04-03 08:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_alter_auction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 4, 3, 10, 53, 24, 524412)),
        ),
    ]

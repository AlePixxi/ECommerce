# Generated by Django 4.1 on 2023-02-03 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_bid_comment_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='auction',
        ),
        migrations.AddField(
            model_name='auction',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auctions.category'),
        ),
    ]

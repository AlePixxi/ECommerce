# Generated by Django 4.1 on 2023-02-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_category_auction_auction_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='url_image',
            field=models.CharField(max_length=128, null=True),
        ),
    ]

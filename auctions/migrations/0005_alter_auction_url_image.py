# Generated by Django 4.1 on 2023-02-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auction_url_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='url_image',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]

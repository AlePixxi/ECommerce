from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime

class User(AbstractUser):
    watchlist = models.ManyToManyField("Auction", null=True, blank=True)

class Category(models.Model):
    category_name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.category_name

class Bid(models.Model):
    value = models.FloatField(default=0)
    bidder = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.value} for {self.auction.title}"

class Auction(models.Model):
    creator = models.ForeignKey("User", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=140)
    url_image = models.CharField(max_length=128, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=datetime.now())
    active = models.BooleanField(default=True)
    offer = models.FloatField(default=0)
    bid = models.OneToOneField(Bid, on_delete=models.CASCADE, default=0)

    def delete(self, *args, **kwargs):
        self.bid.delete()
        super().delete(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title} in date: {self.date}"




class Comment(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE, null=True)
    auction = models.ForeignKey("Auction", on_delete=models.DO_NOTHING, null=True)
    message = models.CharField(max_length=140, null=True)

    def __str__(self) -> str:
        return f"{self.author} comments in: {self.auction}"

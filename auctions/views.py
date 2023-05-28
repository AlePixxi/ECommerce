from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction, Bid, Category, Comment


def index(request):
    auctions = Auction.objects.filter(active=True)

    context = {
        "auctions": auctions,
        "bids": Bid.objects.all()
    }

    return render(request, "auctions/index.html", context=context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url="login")
def create_auction(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image_url = request.POST.get("image")
        category = request.POST.get("category")

        u = User.objects.get(id=request.user.id)
        price = request.POST.get("offer")
        print(price)

        if title != "" and description != "":
            actual_bid = Bid.objects.create(value=price, bidder=request.user)
            actual_bid.save()
            new_auction = Auction.objects.create(creator=u,title=title, description=description, 
                                                url_image=image_url, category=Category.objects.get(category_name=category),
                                                offer=price,
                                                bid=actual_bid)
            new_auction.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create_auction.html", context= {"message": "title or description not valid"})
        

    return render(request, "auctions/create_auction.html", context= {"category_list":Category.objects.all()})


def view_watchlist(request):
    u = User.objects.get(id=request.user.id)
    watchlist = u.watchlist.all()

    return render(request, "auctions/watchlist.html", context={"watchlist": watchlist})

def add_watchlist(request, id):
    auction = Auction.objects.get(id=id)
    u = User.objects.get(id=request.user.id)
    u.watchlist.add(auction)
    u.save()
    return HttpResponseRedirect(reverse("watchlist"))

def delete_auction(request, id):
    auction = Auction.objects.get(id=id)
    if request.user.id == auction.creator.id:
        auction.active = False
        auction.save()
        return HttpResponseRedirect(reverse("view-auction", args=id))
    return HttpResponse("User not allowed")

def remove_watchlist(request, id):
    auction = Auction.objects.get(id=id)
    u = User.objects.get(id=request.user.id)
    u.watchlist.remove(auction);
    return HttpResponseRedirect(reverse("watchlist"))

def view_auction(request, id):

    auction = Auction.objects.get(id=id)
    comments = Comment.objects.filter(auction=auction)


    try:
        u = User.objects.get(id=request.user.id)
        watchlist_element = u.watchlist.get(id=id)
    except:
        watchlist_element = None

    if request.method == "POST":
    
        actual_value = auction.bid.value
        new_bid = float(request.POST.get("new_bid"))
        
        if new_bid > actual_value:
            auction.bid.value = new_bid
            auction.bid.bidder = u
            auction.bid.save()
            auction.save()
        else:
            messages.error(request, "Your bid si too low")

    return render(request, "auctions/view_auction.html", context={"auction": auction, "user_watchlist": watchlist_element, "comments": comments})

def add_comment(request, id):

    author = User.objects.get(id=request.user.id)
    auction = Auction.objects.get(id=id)
    message = request.POST.get("message")

    new_comment = Comment.objects.create(
        author=author,
        auction=auction,
        message=message
    )
    new_comment.save()

    return HttpResponseRedirect(reverse("view-auction", args=id))


def categories_page(request):

    category_list = Category.objects.all()

    return render(request, "auctions/categories.html", context={"category_list": category_list})

def view_category(request, cat):
    category = Category.objects.get(category_name=cat)
    auction_list = Auction.objects.filter(category=category)
    print(category)
    return render(request, "auctions/view_category.html", context={"auction_list": auction_list})


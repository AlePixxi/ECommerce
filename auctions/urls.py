from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories_page, name="categories"),
    path("categories/<str:cat>", views.view_category, name="view-category"),
    path("create-auction", views.create_auction, name="create-auction"),
    path("view-auction/<str:id>", views.view_auction, name="view-auction"),
    path("watchlist", views.view_watchlist, name="watchlist"),
    path("view-auction/<str:id>/add-to-watchlist", views.add_watchlist, name="add-watchlist"),
    path("view-auction/<str:id>/remove-from-watchlist", views.remove_watchlist, name="remove-watchlist"),
    path("view-auction/<str:id>/delete-auction", views.delete_auction, name="delete-auction"),
    path("view-auction/<str:id>/add-comment", views.add_comment, name="add-comment"),
]

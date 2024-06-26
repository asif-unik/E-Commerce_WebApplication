from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name = "ShopHome"),
    path("about/", views.about,name = "about"),
    path("products/<int:myid>", views.productView,name = "ProductView"),
    path("contact/", views.contact,name = "contactus"),
    path("tracker/", views.tracker,name = "tracker"),
    path("search/", views.search,name = "search"),
    path("checkout/", views.checkout,name = "checkout"),
   
]

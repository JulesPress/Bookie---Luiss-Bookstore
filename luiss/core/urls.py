"""
URL configuration for luiss project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.search, name="search"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('change_quantity/<str:product_id>/', views.change_quantity, name='change_quantity'),
    path('remove_from_cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('category/<int:pk>', views.category, name="category"),
    path('single_book/<int:pk>', views.single_book, name="single_book"),
    path('books/', views.books, name="books"),
    path('categories/', views.categories, name="categories"),
    path('about/', views.about, name="about"),
    path('frontpage/', views.frontpage, name='frontpage'),

]

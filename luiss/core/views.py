from django.db.models import Q
from django.shortcuts import render, redirect
from .cart import Cart
from .models import Product, Category


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart_view')


def change_quantity(request, product_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1

        cart = Cart(request)
        cart.add(product_id, quantity, True)
    return redirect('cart_view')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')


def cart_view(request):
    cart = Cart(request)

    return render(request, 'core/cart_view.html', {
        'cart': cart,
    })


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(
        Q(title__icontains=query
        or
        Q(description__icontains=query)
    ))
    return render(request, 'core/search.html', {
        'query': query,
        'products': products,
    })


def frontpage(request):
    products = Product.objects.all()[0:4]
    categories = Category.objects.all()
    return render(request, 'core/frontpage.html',{
        'products': products,
        'categories': categories,
    })


def books(request):
    products = Product.objects.all()
    return render(request, 'core/books.html', {
        'products': products
    })

def single_book(request, pk):
    return render(request, 'core/single_book.html', {
        'product': Product.objects.get(pk=pk),
    })

def category(request, pk):
    return render(request, 'core/category.html', {
        'category': Category.objects.get(pk=pk),
    })

def categories(request):
    categories = Category.objects.all()
    return render(request, 'core/categories.html', {
        'categories': categories
    })

def about(request):
    return render(request, 'core/about.html')


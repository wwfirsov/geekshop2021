from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static
import os
import json
import random

from basketapp.models import Basket
from mainapp.models import Products, ProductCategory

# Create your views here.

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []

module_dir = os.path.dirname(__file__,)

menu = [
        {'href': 'index', 'name': 'главная'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
]

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

def get_hot_product():
    products = Products.objects.all()

    return random.sample(list(products), 1)[0]


def index(request):
    context = {'title':'Магазин', 'menu':menu}
    return render(request, "mainapp/index.html", context)

def get_same_products(hot_product):
    same_products = Products.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products


def products(request, pk=None):
    print(pk)

    title = 'Продукты'
    links_menu = ProductCategory.objects.all()[:6]

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Products.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Products.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'menu': menu,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)


    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
        'menu': menu,
    }

    return render(request, 'mainapp/products.html', content)

def contact(request):
    context = {'title': 'Контакты', 'menu':menu}
    return render(request, "mainapp/contact.html", context)

def main(request):
     title = 'главная'
     product = Products.objects.all()[:6]
     content = {'title': title,
                'links_menu': links_menu,
                'products': product,
                'menu': menu,
                }
     return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'продукты'

    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', context)
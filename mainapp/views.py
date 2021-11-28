from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'title':'Магазин'}
    return render(request, "mainapp/index.html", context)

def products(request):
    context = {'title': 'Продукты'}
    return render(request, "mainapp/products.html", context)

def contact(request):
    context = {'title': 'Контакты'}
    return render(request, "mainapp/contact.html", context)

def context(request):
    context = {
        'title':'test context',
        'header':'Добро пожаловать на сайт',
        'username':'Джон',
        'products': [
            {'name':'Стулья','price':6789},
            {'name': 'Диваны', 'price': 12389},
            {'name': 'Столы', 'price': 16789},
        ]
    }
    return render(request, "mainapp/test_context.html", context)

def menu(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    return render(request, 'inc_categories_menu.html', links_menu)
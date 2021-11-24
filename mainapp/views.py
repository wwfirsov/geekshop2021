from django.shortcuts import render
from django.templatetags.static import static
import os
import json
from mainapp.models import Products, ProductCategory

# Create your views here.

module_dir = os.path.dirname(__file__,)

links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

menu = [
        {'href': 'index', 'name': 'главная'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
]

def index(request):
    context = {'title':'Магазин', 'menu':menu}
    return render(request, "mainapp/index.html", context)

def products(request, pk=None):
    print(pk)
    file_path = os.path.join(module_dir, 'fixtures/products.json')
    products = json.load(open(file_path, encoding='utf-8'))



    title = 'Продукты'
    product = Products.objects.all()[:4]
    content = {'title': title,
        'links_menu': links_menu,
        'products': product,
        'menu': menu,
    }
    # content = {'title': title, 'products': product}


    return render(request, 'mainapp/products.html', content)

def contact(request):
    context = {'title': 'Контакты', 'menu':menu}
    return render(request, "mainapp/contact.html", context)

def main(request):
     title = 'главная'
     product = Products.objects.all()[:4]
     content = {'title': title,
                'links_menu': links_menu,
                'products': product,
                'menu': menu,
                }
     return render(request, 'mainapp/products.html', content)

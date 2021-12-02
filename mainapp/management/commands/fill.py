import json
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Products



def load_from_json(file_name):
    with open(f"{settings.BASE_DIR}/json/{file_name}.json", 'r', encoding="utf-8") as json_file:
        return json.load(json_file)

class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)

        products = load_from_json('products')

        Products.objects.all().delete()
        for products in products:
            category_name = products['category']
            category_item = ProductCategory.objects.get(name=category_name)
            products['category'] = category_item
            Products.objects.create(**products)

        ShopUser.objects.create_superuser('django', password='geekbrains', age=18)


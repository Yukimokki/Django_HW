from django.core.management import BaseCommand
from catalog.models import Product, Category
import json
from django.db import connection

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog/management/commands/category.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('catalog/management/commands/product.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):
        self.clean_database()
        self.reset_sequences()

# Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

# Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_fields = category["fields"]
            category_for_create.append(Category(**category_fields))
            # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)


# Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_fields = product["fields"]
            category_id = product_fields.get('category')
            category_instance = Category.objects.get(pk=category_id)
            if 'category' in product_fields:
                del product_fields['category']
            product_for_create.append(Product(category=category_instance, **product_fields))

        def clean_database(self):
            """Очищаем базу данных"""
        Product.objects.all().delete()
        Category.objects.all().delete()

        def reset_sequences(self):
            """Сбрасываем автоинкрементные значения таблиц"""
            with connection.cursor() as cursor:
                cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")
                cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")
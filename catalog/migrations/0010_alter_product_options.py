# Generated by Django 4.2.2 on 2024-10-19 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0009_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name"],
                "permissions": [
                    ("can_edit_category", "can change category"),
                    ("can_edit_description", "can edit description"),
                    ("can_edit_publication", "can change publication"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
# Generated by Django 4.2.2 on 2024-10-19 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name"],
                "permissions": [
                    ("can_edit_category", "can edit breed"),
                    ("can_edit_description", "can edit description"),
                    ("can_edit_publication", "can change publication"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="published"),
        ),
    ]

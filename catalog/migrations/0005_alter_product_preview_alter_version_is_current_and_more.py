# Generated by Django 5.1 on 2024-10-05 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="preview",
            field=models.ImageField(
                help_text="Upload photo",
                upload_to="products/media",
                verbose_name="превью продукта",
            ),
        ),
        migrations.AlterField(
            model_name="version",
            name="is_current",
            field=models.BooleanField(default=False, verbose_name="current_version"),
        ),
        migrations.AlterField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="versions",
                to="catalog.product",
                verbose_name="Version",
            ),
        ),
    ]

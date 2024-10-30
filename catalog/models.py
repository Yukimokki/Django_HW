from django.db import models

from users.models import User, NULLABLE


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="название категории",
        help_text="Category name",
    )
    description = models.TextField(
        verbose_name="описание категории",
        help_text="describe the category",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="название продукта",
        help_text="Product's name",
    )
    description = models.TextField(
        verbose_name="описание продукта",
        help_text="describe the product",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="products/media",
        #blank=True,
        #null=True,
        verbose_name="превью продукта",
        help_text="Upload photo",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="категория продукта",
        help_text="select product category",
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата добавления",
        help_text="date when added",
    )

    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="date when changed",
    )

    views_counter = models.PositiveIntegerField(
        verbose_name="visits counter",
        help_text="Number of views",
        default=0
    )

    is_published = models.BooleanField(default=False, verbose_name="published")

    owner = models.ForeignKey(
        User,
        verbose_name="Owner",
        help_text="print Products's owner name",
        on_delete=models.SET_NULL,
        **NULLABLE)

    # manufactured_at = models.DateField(
    #     blank=True,
    #     null=True,
    #     verbose_name="Дата производства",
    #     help_text="manufacturing date"
    # )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
        permissions = [
            ("can_change_category", "can change category"),
            ("can_edit_description", "can edit description"),
            ("can_edit_publication", "can change publication")
        ]

class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Version",)

    version_number = models.CharField(
        max_length=50,
        verbose_name="Version number",
        help_text="product version number",
    )

    version_name = models.CharField(
        max_length=50,
        verbose_name="Version name",
        help_text="product version name",
    )

    is_current = models.BooleanField(
        default=False, verbose_name="current_version",
    )
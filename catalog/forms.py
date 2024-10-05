from django.forms import ModelForm, BooleanField
from django.utils import timezone
from catalog.models import Category, Product, Version
from django.core.exceptions import ValidationError


class StyleFormMixin:
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"

class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("views_counter",)

    def clean_version_text(self):
        list_forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        product_name = self.cleaned_data["name"].split()
        for item in list_forbidden_words:
            if item in product_name:
                raise ValidationError("Invalid name")
            return product_name

        product_text = self.cleaned_data["description"].split()
        for item in list_forbidden_words:
            if item in product_text:
                raise ValidationError("Invalid description")
            return product_name

class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"



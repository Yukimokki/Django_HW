from django.forms import ModelForm, BooleanField
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

    def clean_name(self):
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
        product_name = self.cleaned_data["name"]
        for item in list_forbidden_words:
            if item in product_name:
                raise ValidationError("Invalid name")
        return product_name


    def clean_description(self):
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
        product_description = self.cleaned_data["description"]
        for item in list_forbidden_words:
            if item in product_description:
                raise ValidationError("Invalid description. Are you a scammer?")
        return product_description



class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"



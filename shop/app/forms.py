from django import forms
from django.forms import ModelForm
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_price(self):
        price = self.cleaned_data.get('price')  # Use cleaned_data
        if price and price > 1000:
            raise ValidationError("Product is too expensive")
        return price

    def clean_description(self):
        description = self.cleaned_data.get('description')  # Use cleaned_data
        if description and len(description) <= 20:
            raise ValidationError("Product must have a good description")
        return description

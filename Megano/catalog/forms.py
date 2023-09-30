from django import forms
from django.contrib.auth.models import Group
from .models import Product
from order.models import Order


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = 'title', 'price', 'description', 'images'

    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': False}),
    )


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = 'fullName', 'address', 'phone', 'products'


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name']


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()

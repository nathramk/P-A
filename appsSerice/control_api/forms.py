from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from appsSerice.control.models.producto import Product
from appsSerice.control.models.categoria import Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name_category', 'category_logo']


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

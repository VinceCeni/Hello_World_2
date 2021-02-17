from django.forms import ModelForm
from .models import Product
from .forms import ProductForm

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
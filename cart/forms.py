from django import forms
from catalog.models import Product



PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in (2, 10)]
class CartAddProductForm(forms.Form):    
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
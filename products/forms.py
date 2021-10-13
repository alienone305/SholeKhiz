from django import forms
from products.models import ProductsModel


class ProductsForm(forms.ModelForm):


    class Meta:
        model = ProductsModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'نام محصول'},),
            'picture': forms.FileInput(attrs={'class':'uk-button','id':'picture'},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'5','placeholder':'توضیحات'},),
            'cataloge': forms.FileInput(attrs={'class':'uk-button','id':'cataloge'},),
        }

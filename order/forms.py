from django import forms
from order.models import OrderingModel


class OrderingForm(forms.ModelForm):

    class Meta:
        model = OrderingModel
        fields = ('description', 'number')
        widgets = {
            'number': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'تعداد'},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'توضیحات'},),
        }

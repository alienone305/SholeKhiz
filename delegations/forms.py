from django import forms
from delegations.models import DelegationModel

class DelegationForm(forms.ModelForm):
    class Meta():
        model = DelegationModel
        fields = ('province','address','phone_number')
        widgets = {
            'province': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'استان'},),
            'phone_number': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'شماره تماس'},),
            'address': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'2','placeholder':'آدرس'},),
        }

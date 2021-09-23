from django import forms
from company.models import ContactUsModel

class ContactUsForm(forms.ModelForm):
    class Meta():
        model = ContactUsModel
        fields = ('name','email','phone_number','request')
        widgets = {
            'name': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نام و نام خانوادگی'},),
            'phone_number': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'شماره تماس'},),
            'request': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'متن درخواست یا پیشنهاد'},),
            'email': forms.EmailInput(attrs={'class':'uk-input fHarmattan','placeholder':'ایمیل'},),

        }

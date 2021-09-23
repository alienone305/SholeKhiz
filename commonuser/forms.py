from django import forms
from commonuser.models import CommonUserModel
from django.core import validators


class CommonUserForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def __init__(self, *args, **kwargs):
        super(CommonUserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CommonUserModel
        fields = ('address',)
        widgets = {
            'address': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'3','placeholder':'آدرس',}),
        }


class ConfirmationForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'کد ارسالی به شماره تلفن','id': 'code',}))
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

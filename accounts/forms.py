from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserModel
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm

class UserForm(UserCreationForm):
    '''form for creating a user'''


    terms = forms.BooleanField(
    error_messages={'required': 'لطفا شرایط و قوانین سایت را مطالعه کرده و تیک موافقت را بزنید'},
    widget=forms.CheckboxInput(attrs={'class': 'uk-checkbox'})
    )

    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'uk-input fHarmattan','placeholder':'شماره تلفن مثال 9141234567','id':'username','onblur':'checkLength(this)'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
'class':'uk-input fHarmattan redC-text','placeholder':'رمز عبور'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
'class':'uk-input fHarmattan redC-text','placeholder':'تکرار رمز عبور'
        }))

    class Meta(UserCreationForm):
        model = UserModel
        fields = ('username','email',
                  'name','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'شماره همراه','id':'username','onblur':'checkLength(this)'},),
            'name': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'نام و نام خانوادگی'},),
        }


class TypesForm(forms.Form):

    commonusers = forms.BooleanField(required=False)

    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


class UserUpdateForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = UserModel
        fields = ('first_name','email','last_name')
        widgets = {
            'email': forms.TextInput(attrs={'id':'email'}),
            'first_name': forms.TextInput(attrs={'id':'first_name'}),
            'last_name': forms.TextInput(attrs={'id':'last_name'}),
        }


class UserLoginForm(AuthenticationForm):


    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'uk-input fHarmattan redC-text','placeholder':'شماره همراه','id':'username','onblur':'checkLength(this)'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
'class':'uk-input fHarmattan redC-text','placeholder':'رمز عبور'
        }
))
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)


class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'uk-input fHarmattan','placeholder':'رمز فعلی','id':'current_password'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'uk-input fHarmattan','placeholder':'رمز جدید','id':'new_password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'uk-input fHarmattan','placeholder':'تکرار رمز جدید','id':'confirm_password'}))
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


class ForgotPasswordForm(forms.Form):
    phone_number = forms.CharField(required = True, widget=forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مثال 9141234567','id':'username','onblur':'checkLength(this)'}))
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

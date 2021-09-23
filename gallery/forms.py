from django import forms

# handmade
from gallery.models import GalleryModel

class GalleryForm(forms.ModelForm):
    class Meta():
        model = GalleryModel
        fields = ('picture','description')
        widgets = {
            'picture': forms.FileInput(attrs={'class':'uk-button',},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'2','placeholder':'توضیحات'},),
        }

from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    original_img = forms.TextInput (attrs={'id': 'media', 'type':'button', 'class':'btn btn-primary js-upload-photos'})

    class Meta:
        model = Images
        fields = ['original_img', 'image_format']

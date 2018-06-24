from django import forms
from .models import Document


class DocumentCreationForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('username', 'email')


class DocumentChangeForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('username', 'email')

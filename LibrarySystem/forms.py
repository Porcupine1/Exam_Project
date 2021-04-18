from django import forms
from .models import SoftBook

class SoftBookForm(forms.ModelForm):
    class Meta:
        model = SoftBook
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'book_title',
                'name': 'book_title'}),
            'description': forms.TextInput(attrs={
                'id': 'book_description',
                'name': 'book_description'}),
            'image': forms.FileInput(attrs={
                'class': 'uploadBtn',
                'name': 'imgUploadBtn'}),
            'book': forms.FileInput(attrs={
                'class': 'uploadBtn',
                'name': 'bookUploadBtn'}),
        }

        labels = {
            'book': ('Browse For Pdf File'),
            'image': ('Browse For Image')
        }
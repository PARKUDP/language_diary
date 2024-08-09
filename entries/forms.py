from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']
        labels = {
            'title': 'タイトル:',
            'content': '本文:'
        }
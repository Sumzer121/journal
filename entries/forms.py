from django import forms
from .models import JournalEntry

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 80})
        }
        labels = {
            'title': "Title:",
            'content': 'Content:',
        }

        error_messages = {
            'title': {'required': "Please enter a title."},
            'content': {'required': "Please enter content."}
        }
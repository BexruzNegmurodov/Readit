from django import forms
from .models import Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('blog', 'full_name', 'email', 'message', 'question')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'email'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'message'
        })
        self.fields['question'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Write if you have any questions...',
            'rows': '1'
        })





from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'subject',
            'reason',
            'message',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Full Name',
                'class': 'form-control',
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Your Email Address',
                'class': 'form-control',
            }),

            'subject': forms.TextInput(attrs={
                'placeholder': 'What would you like to discuss?',
                'class': 'form-control',
            }),

            'reason': forms.Select(attrs={
                'class': 'form-control',
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Write your message here...',
                'rows': 5,
                'class': 'form-control',
            }),
        }

        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'reason': 'Reason for Contacting',
            'message': 'Your Message',
        }
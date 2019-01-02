# from django import forms
# from myzehut_app.models import User


# class ContactForm(forms.ModelForm):
#   class Meta:
#     model   = User
#     fields  = ['subject', 'email', 'text']
#     widgets = {
#       'subject': forms.TextInput(attrs={
#         'id': 'contact-subject',
#         'placeholder': 'subject',
#         'required': True
#       }),
#       'email': forms.EmailInput(attrs={
#         'id': 'contact-email',
#         'placeholder': 'email',
#         'required': True
#       }),
#       'text': forms.Textarea(attrs={
#         'id': 'contact-text',
#         'placeholder': 'Write a contact here...',
#         'required': True
#       }),
#     }
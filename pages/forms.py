from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=225, widget=forms.TextInput(attrs={'placeholder': "Your Name"}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder":"Subject"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Message"}))

from django import forms
from core.models import ContactUs, NewsletterSubscription, Comment
from django.contrib.auth.models import User
from django.forms import ModelForm




class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name',  'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınızı daxil edin.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email-i daxil edin.'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mövzu xətti.'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınızı yazın', 'rows': 4}),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ["email"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'website', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email *'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your Website'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment *', 'rows': 5}),
        }

class UserForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self ):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
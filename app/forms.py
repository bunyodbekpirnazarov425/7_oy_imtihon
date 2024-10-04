from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Book, Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'price', 'cover_image', 'description']

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            "id": "exampleFormControlTextarea1",
            'class': "form-control form-control-lg",
            'placeholder': "Write a comment",
        }
    ))
    class Meta:
        model = Comment
        fields = ['text']

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            "id": "form3Example1c",
            'class': "form-control form-control-lg",
            'placeholder': "Username",
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "id": "form3Example3c",
            'class': "form-control form-control-lg",
            'placeholder': "Email",
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs= {
            "id": "form3Example4c",
            'class': "form-control form-control-lg",
            'placeholder': "Password",
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "id": "form3Example4cd",
            'class': "form-control form-control-lg",
            'placeholder': "Repeat Password",
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            "id": "form2Example1",
            'class': "form-control",
            'placeholder': "Username",
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "id": "form2Example2",
            'class': "form-control",
            'placeholder': "Password",
        }))

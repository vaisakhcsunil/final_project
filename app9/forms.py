from django import forms
class SignupForm(forms.Form):
    username=forms.CharField(label="username",max_length=200)
    email=forms.EmailField(label="email",max_length=200)
    password=forms.CharField(widget=forms.PasswordInput,label="password",max_length=200)
    password_confirm=forms.CharField(widget=forms.PasswordInput,label='password_confirm',max_length=200)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

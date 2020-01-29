from django import forms

# Create your models here.
class NewRegister(forms.Form):
    first_name =forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    phone = forms.IntegerField()    
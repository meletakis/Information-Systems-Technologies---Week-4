from django import forms

class CreateUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100,required = True)
    email = forms.EmailField(label='Email',required = True)
    password = forms.CharField(label='Password', max_length=100,required = True)
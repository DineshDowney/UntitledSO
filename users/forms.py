from django import forms
from django.contrib.auth.models import User
class Register(forms.Form):
    fname = forms.CharField(label="First Name",widget=forms.TextInput(
        attrs={"placeholder":"Your first name"}))
    lname = forms.CharField(label="Last Name",widget=forms.TextInput(
        attrs={"placeholder": "Your last name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"placeholder": "username@xyz.com"}), label="E-Mail Address")
    mob_num = forms.DecimalField(
        max_digits=10, decimal_places=0, label="Mobile Number")
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(
        attrs={"placeholder": "********"}))
    password2 = forms.CharField(label="Password confirmation",widget=forms.PasswordInput(
        attrs={"placeholder": "********"}),
        help_text="Enter the same password as above, for verification.")
        
    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password2 != password1:
            raise forms.ValidationError("Passwords must match")
        return data

class LoginForm(forms.Form):
    uname = forms.CharField(label="Username", widget=forms.TextInput(
                attrs={"placeholder": "Username"}))
    #email = forms.EmailField(widget=forms.EmailInput(
     #   attrs={"placeholder": "username@xyz.com"}), label="E-Mail Address")
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"placeholder": "********"}))

    def clean(self):
        data = self.cleaned_data
        return data
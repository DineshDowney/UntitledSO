from users.models import Profile
from django.core.files.images import get_image_dimensions
from django import forms
from django.contrib.auth.models import User
class Register(forms.Form):
    fname = forms.CharField(label="First Name",widget=forms.TextInput(
        attrs={"placeholder":"Your first name"}))
    lname = forms.CharField(label="Last Name",widget=forms.TextInput(
        attrs={"placeholder": "Your last name"}))
  #  username = forms.CharField(label="UserName", widget=forms.TextInput(
   #     attrs={"placeholder": "Your desired username"}))
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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio']
    image = forms.ImageField()
    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        try:
            w, h = get_image_dimensions(avatar)
            #validating dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is  %s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, GIF or PNG image.')

            #validate file size
            if len(avatar) > (2048 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 2MB.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass
        return avatar

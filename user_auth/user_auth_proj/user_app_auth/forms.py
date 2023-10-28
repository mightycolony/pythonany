from django import forms 
from django.contrib.auth.models import User
from user_app_auth.models import UserProfileInfo


#seperate form form each User and userprofileinfo
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
    
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields=('protfolio_site','profile_picture')
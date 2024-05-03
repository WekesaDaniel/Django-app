#created this file it did not come inbuilt in django
   
# forms.py
from django import forms
from .models import UserDetail

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['name', 'email', 'phone_number', 'post_office_box', 'house_address', 'password']

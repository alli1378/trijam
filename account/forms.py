from django import forms
from django.db import models
from django.forms import fields
from .models import User
from django.contrib.auth.forms import UserCreationForm
from translate.models import Translate

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
class ProfileForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user')
        super(ProfileForm,self).__init__(*args,**kwargs)
        self.fields['username'].help_text=False
        self.fields['email'].help_text=False
        if not user.is_superuser:
            self.fields['username'].disabled=True
            self.fields['email'].disabled=True
            self.fields['is_translator'].disabled=True
        
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','is_translator']
class FieldForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user')
        super(FieldForm,self).__init__(*args,**kwargs)
        if not user.is_superuser:
            self.fields['language'].disabled=True
            self.fields['title'].disabled=True
            self.fields['author'].disabled=True
            self.fields['customer'].disabled=True
            self.fields['price'].disabled=True
            self.fields['filesend'].disabled=True
            # self.fields['filerisive'].disabled=True
            self.fields['type'].disabled=True
        
    class Meta:
        model=Translate
        fields=['language', 'title','author','customer',  'price', 'filesend' ,'filerisive' , 'is_finished','type']
class FieldFormAll(forms.ModelForm):
    class Meta:
        model=Translate
        fields=['language', 'title', 'price', 'customer','author','filesend' ,'filerisive' , 'is_finished','type']
from django.contrib.auth.models import User
from django import forms
from .models import Information


class UserFrom(forms.ModelForm):
    class meta:
        model=User
        field = ['first_name','last_name']

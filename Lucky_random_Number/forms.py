from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class Form_Import_Data (forms.ModelForm):
    
    class Meta:
        model = Round_Tauthong
        fields = "__all__"
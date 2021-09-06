from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 

class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"

class GameForm(forms.ModelForm):

    class Meta:
       model = GameModel
       fields = '__all__'
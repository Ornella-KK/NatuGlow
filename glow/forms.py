from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['words']
        exclude = ['user']

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name','products','description']
        exclude = ['review','user','category']

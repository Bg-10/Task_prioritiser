from django import forms
from .models import to_do
 
 
class todoform(forms.ModelForm):
    class Meta:
        model = to_do
        fields = "__all__"
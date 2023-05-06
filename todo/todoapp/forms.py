from django import forms
from .models import User
class Form(forms.ModelForm):
    
    class Meta:
        
        model = User
        fields = ['task_name']
        widgets = {
            'task_name' : forms.TextInput(attrs = {'class':'form-control'})
        }

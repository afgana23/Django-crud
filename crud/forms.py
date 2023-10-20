from django import forms
from crudmodel.models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Myform(forms.Form):
     num1=forms.CharField(label="number1")





class AddUSerForm(forms.ModelForm):
 
 class Meta:
        model=MyUser
        fields=('username','email','password')
class MyModelForm(forms.ModelForm):
    class Meta:
        model= MyUser
        fields=('username','email','password')
        label=('username','email','password')
      

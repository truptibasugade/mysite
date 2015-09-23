from users.models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.HiddenInput(),initial='pwd',required=False)
	username = forms.CharField(widget=forms.HiddenInput(), initial='uname',required=False)
	email = forms.CharField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	
    
	class Meta:
		model = User
		fields = ('first_name','last_name','email')


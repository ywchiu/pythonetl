from django import forms
from .models import Join
class EmailForm(forms.Form):
	email = forms.EmailField()

class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields = ["email",]
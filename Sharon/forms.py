# sharon/forms.py
# Sharon/forms.py
from django import forms
from .models import UserInformation

class UserInformationForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = ['name', 'education', 'job', 'programming']



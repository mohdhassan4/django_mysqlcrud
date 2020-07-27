from django import forms
from crudapp.models import employee

class employeeform(forms.ModelForm):
    class meta:
        model=employee
        fields="__all__"
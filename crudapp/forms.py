from django import forms
from crudapp.models import employee

class EmployeeForm(forms.ModelForm):
    class meta:
        model=employee
        fields="__all__"
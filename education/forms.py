from django import forms
from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    model = Application
    fields = ['first_name', 'other_names', 'study', 'level', 'gender', 'campus', 'course', 'Date_of_birth', 'email',
    'phone', 'residence', 'nationality', 'where', 'file1', 'file2', 'file3', 'other_contact' ]

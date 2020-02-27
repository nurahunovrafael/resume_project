from django import forms
from .models import Resume, Job, Education

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

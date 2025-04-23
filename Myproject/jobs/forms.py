from django import forms
from .models import JobApplication

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'job', 'email', 'salary_expectation', 'about', 'resume', 'cover_letter']
        widgets = {
            'about': forms.Textarea(attrs={'rows': 4}),
        }

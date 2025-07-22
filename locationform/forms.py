
from django import forms
from .models import  AttendanceSubmission  
class AttendanceSubmissionForm(forms.ModelForm):
    class Meta:
        model = AttendanceSubmission
        fields = ['name', 'email', 'present', 'location_accuracy']

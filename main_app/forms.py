from django.forms import ModelForm
from django import forms
from .models import Dose

class DoseForm(ModelForm):
  class Meta:
    model = Dose
    fields = ['date', 'dosage', 'time']
    widgets = { 
      'time': forms.TimeInput(attrs={'type': 'time'})
    }
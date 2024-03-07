from django.forms import ModelForm
from .models import Dose

class DoseForm(ModelForm):
  class Meta:
    model = Dose
    fields = ['date', 'dosage', 'time']
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Drug
from .forms import DoseForm

# Create your views here
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def drug_index(request):
  drugs = Drug.objects.all()
  return render(request, 'drugs/index.html', { 'drugs': drugs })


def drug_detail(request, drug_id):
  drug = Drug.objects.get(id=drug_id)
  dose_form = DoseForm()
  return render(request, 'drugs/detail.html', { 
    'drug': drug,
    'dose_form': dose_form
    })

class DrugCreate(CreateView):
  model = Drug
  fields = ['name', 'form', 'duration', 'notes']
  success_url = '/medications/'

class DrugUpdate(UpdateView):
  model = Drug
  fields = ['name', 'form', 'duration', 'notes']

class DrugDelete(DeleteView):
  model = Drug
  success_url = '/medications/'
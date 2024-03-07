from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Drug

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
  return render(request, 'drugs/detail.html', { 'drug': drug })

class DrugCreate(CreateView):
  model = Drug
  fields = ['name', 'form', 'duration', 'notes']
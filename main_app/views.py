from django.shortcuts import render
from .models import Drug

# Create your views here
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def drug_index(request):
  drugs = Drug.objects.all()
  return render(request, 'drugs/index.html', { 'drugs': drugs })
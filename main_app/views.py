from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Drug, Photo
from .forms import DoseForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'brianna-mindful-dose'

# Create your views here
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def drug_index(request):
  drugs = Drug.objects.filter(user=request.user)
  return render(request, 'drugs/index.html', { 'drugs': drugs })

@login_required
def drug_detail(request, drug_id):
  drug = Drug.objects.get(id=drug_id)
  dose_form = DoseForm()
  return render(request, 'drugs/detail.html', { 
    'drug': drug,
    'dose_form': dose_form
    })

class DrugCreate(LoginRequiredMixin, CreateView):
  model = Drug
  fields = ['name', 'form', 'duration', 'notes']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DrugUpdate(LoginRequiredMixin, UpdateView):
  model = Drug
  fields = ['form', 'duration', 'notes']

class DrugDelete(LoginRequiredMixin, DeleteView):
  model = Drug
  success_url = '/medications/'

@login_required
def add_dose(request, drug_id):
  form = DoseForm(request.POST)
  if form.is_valid():
    new_dose = form.save(commit=False)
    new_dose.drug_id = drug_id
    new_dose.save()
  return redirect('drug-detail', drug_id=drug_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('drug-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def add_photo(request, drug_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, drug_id=drug_id)
      # Remove old photo if it exists
      drug_photo = Photo.objects.filter(drug_id=drug_id)
      if drug_photo.first():
        drug_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('drug-detail', drug_id=drug_id)
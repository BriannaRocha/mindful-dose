from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('medications/', views.drug_index, name='drug-index'),
  path('medications/<int:drug_id>/', views.drug_detail, name='drug-detail'),
  path('drugs/create/', views.DrugCreate.as_view(), name='drug-create'),
]
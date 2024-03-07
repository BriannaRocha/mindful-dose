from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('drugs/', views.drug_index, name='drug-index'),
  path('drugs/<int:drug_id>/', views.drug_detail, name='drug-detail'),
]
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('medications/', views.drug_index, name='drug-index'),
  path('medications/<int:drug_id>/', views.drug_detail, name='drug-detail'),
  path('drugs/create/', views.DrugCreate.as_view(), name='drug-create'),
  path('drugs/<int:pk>/update/', views.DrugUpdate.as_view(), name='drug-update'),
  path('drugs/<int:pk>/delete/', views.DrugDelete.as_view(), name='drug-delete'),
  path('drugs/<int:drug_id>/add-dose/', views.add_dose, name='add-dose'),
]
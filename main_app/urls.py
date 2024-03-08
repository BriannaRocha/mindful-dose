from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('medications/', views.drug_index, name='drug-index'),
  path('medications/<int:drug_id>/', views.drug_detail, name='drug-detail'),
  path('medications/create/', views.DrugCreate.as_view(), name='drug-create'),
  path('medications/<int:pk>/update/', views.DrugUpdate.as_view(), name='drug-update'),
  path('medications/<int:pk>/delete/', views.DrugDelete.as_view(), name='drug-delete'),
  path('medications/<int:drug_id>/add-dose/', views.add_dose, name='add-dose'),
  path('dose/<int:pk>/update/', views.DoseUpdate.as_view(), name='dose-update'),
  path('dose/<int:pk>/delete/', views.DoseDelete.as_view(), name='dose-delete'),
  path('accounts/signup/', views.signup, name='signup'),
]
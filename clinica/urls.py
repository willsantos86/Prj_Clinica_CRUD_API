from django.urls import path
from clinica import views

urlpatterns = [
    path('', views.PacienteList.as_view(), name='paciente-list'),
    path('create/', views.PacienteCreate.as_view(), name='paciente-create'),
    path('update/<int:pk>/', views.PacienteUpdate.as_view(), name='paciente-update'),
    path('detail/<int:pk>/', views.PacienteDetail.as_view(), name='paciente-detail'),
    path('delete/<int:pk>/', views.PacienteDelete.as_view(), name='paciente-delete'),
]

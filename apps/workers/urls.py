from django.urls import path
from . import views

app_name = 'workers'

urlpatterns = [
    path('', views.list_workers, name='list_workers'),
    path('adicionar/', views.add_worker, name='add_worker'),
    path('editar/<int:id_worker>/', views.edit_worker, name='edit_worker'),
    path('excluir/<int:id_worker>/', views.delete_worker, name='delete_worker'),
]
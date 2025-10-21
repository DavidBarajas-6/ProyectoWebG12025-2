from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('nuevo/', views.nuevo, name='nuevo'),
    path('editar/<int:post_id>/', views.editar, name='editar'),
    path('borrar/<int:post_id>/', views.borrar, name='borrar'),
    path('registro/', views.registro, name='registro'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('funcionario', views.funcionario_list, name='funcionario_list'),
    path('funcionario/', views.funcionario_list, name='funcionario_list'),
    path('funcionario/visualizar/<int:pk>', views.funcionario_view, name='funcionario_view'),
    path('funcionario/novo', views.funcionario_create, name='funcionario_new'),
    path('funcionario/editar/<int:pk>', views.funcionario_update, name='funcionario_edit'),
    path('funcionario/deletar/<int:pk>', views.funcionario_delete, name='funcionario_delete'),
    path('setor', views.setor_list, name='setor_list'),
    path('setor/', views.setor_list, name='setor_list'),
    path('setor/visualizar/<int:pk>', views.setor_view, name='setor_view'),
    path('setor/novo', views.setor_create, name='setor_new'),
    path('setor/editar/<int:pk>', views.setor_update, name='setor_edit'),
    path('setor/deletar/<int:pk>', views.setor_delete, name='setor_delete'),
]
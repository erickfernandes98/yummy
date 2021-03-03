from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.produto_form, name='produto_insert'), # requisições get e post para operações de insert
    path('<int:id>/', views.produto_form, name='produto_update'), # requisições get e post para operações de update
    path('delete/<int:id>/', views.produto_delete, name='produto_delete'),
    path('list/', views.produto_list, name='produto_list') # requisições get para recuperar e mostrar todos os registros
]
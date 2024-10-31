from django.urls import path
from .views import ViewsFilme

""" Configuração das URL que serao exibidas no campo de busca  """

urlpatterns = [
    path('', ViewsFilme, name='viewfilme'),
##    path('imagem/<int:foto_id>', imagem, name='imagem'),
  ##  path('buscar', buscar, name='buscar'),
]
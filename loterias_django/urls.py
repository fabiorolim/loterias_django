from django.contrib import admin
from django.urls import path
from core.views import home, jogar_mega, novo_jogo_mega, \
    listagem_megasena, jogar_quina, novo_jogo_quina, listagem_quina

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home_page'),
    path('jogar_mega/', jogar_mega, name='jogar_mega'),
    path('novo_jogo_mega/', novo_jogo_mega,
         name='novo_jogo_mega'),
    path('listar_mega/', listagem_megasena,
         name='listagem_mega'),
    path('jogar_quina/', jogar_quina, name='jogar_quina'),
    path('novo_jogo_quina/', novo_jogo_quina,
         name='novo_jogo_quina'),
    path('listar_quina/', listagem_quina,
         name='listagem_quina'),
]

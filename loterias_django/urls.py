from django.contrib import admin
from django.urls import path
from core.views import home, jogar_mega, novo_jogo_mega, \
    listagem_megasena

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home_page'),
    path('jogar_mega/', jogar_mega, name='jogar_mega'),
    path('novo_jogo_mega/', novo_jogo_mega,
         name='novo_jogo_mega'),
    path('listar_mega/', listagem_megasena,
         name='listagem_mega')
]

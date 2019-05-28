from django.shortcuts import render
from .negocio import Megasena as Mg
from .models import MegaSena


# Create your views here.
def home(request):
    return render(request, 'home.html')


def novo_jogo_mega(request):
    if request.method == "POST":
        ms = Mg(int(request.POST['quantidade']))
        ms.adiciona_numero()
        megasena = MegaSena(numeros=ms.numeros)
        megasena.save()
        context = {
            'jogo': ms.numeros
        }
    return render(request, 'exibe_jogo_mega.html', context)


def listagem_megasena(request):
    jogos = MegaSena.objects.all()
    context = {
        'jogos': jogos
    }
    return render(request, 'listagem_mega.html', context)


def jogar_mega(request):
    return render(request, 'jogar_mega.html')

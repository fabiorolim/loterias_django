from django.shortcuts import render
from .negocio import Megasena as Mg, Quina as Qui
from .models import MegaSena, Quina


# Create your views here.
def home(request):
    return render(request, 'home.html')


def novo_jogo_mega(request):
    if request.method == "POST":
        ms = Mg()
        ms.sortear(int(request.POST['quantidade']))
        megasena = MegaSena(numeros=ms.sorteados)
        megasena.save()
        context = {
            'jogo': ms.sorteados
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


def jogar_quina(request):
    return render(request, 'jogar_quina.html')


def novo_jogo_quina(request):
    if request.method == "POST":
        qui = Qui()
        qui.sortear(int(request.POST['quantidade']))
        quina = Quina(numeros=qui.sorteados)
        quina.save()

        context = {
            'jogo': qui.sorteados
        }

    return render(request, 'exibe_jogo_quina.html', context)


def listagem_quina(request):
    jogos = Quina.objects.all()
    context = {
        'jogos': jogos
    }
    return render(request, 'listagem_quina.html', context)

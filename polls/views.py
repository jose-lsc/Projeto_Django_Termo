from functools import lru_cache

from django.utils import timezone
import datetime
from django.shortcuts import render, HttpResponse
from django.db.models import F
from .models import Palavra, Usuario, PalavraDia
import random
from django.contrib.auth.decorators import login_required

def sortear_palavra() -> str:
    todas_as_palavras = list(Palavra.objects.all())
    palavra = random.choice(todas_as_palavras)
    PalavraDia.objects.create(
        dia=timezone.now(),
        palavra=palavra,
    )
    return palavra.conteudo


def palavra_do_dia() -> str:
    try:
        # dia_criacao >= hoje menos 24h
        palavra_dia = PalavraDia.objects \
            .filter(dia__gte=timezone.now() - datetime.timedelta(hours=24))[:1] \
            .get()
        return palavra_dia.palavra.conteudo
    except:
        return sortear_palavra()


def lobby(request):
    return render(request, "polls/Lobby.html")


def word_list(request):
    palavras = Palavra.objects.all()
    return render(request, "polls/word_list.html", {"palavras": palavras})



@login_required
def termo(request):

    informacao = list(Palavra.objects.all())
    # [ { conteudo: 'teste'}, { conteudo: 'abcde'}]
    palavra = palavra_do_dia().upper()
    print(palavra)
    #  { conteudo: 'abcde'}
    conjuntoDeLetras = list(palavra)
    palavraTermo = request.session.get("palavraTermo", [''] * 5)
    usuario, created = Usuario.objects.get_or_create(user=request.user)
    acertou = False
    perdeu = False

    # if request.method == 'GET':
    #     request.session['palavraTermo'] = [''] * 5
    #     Usuario.objects.update(vidas = 6)

    if request.method == 'POST':

        resposta = request.POST.get('resposta', '').upper()
        conjuntoDeLetras = list(palavra)
        if resposta == palavra:
            #request.session.flush()
            acertou = True
            request.session['palavraTermo'] = [''] * 5
            Usuario.objects.update(vidas = 6)
            
        else:
            
            letras_corretas = []
            usuario.vidas = F('vidas') -1 
            usuario.save()
            usuario = Usuario.objects.get(user=request.user)
            if usuario.vidas == 0:
                perdeu = True
                request.session['palavraTermo'] = [''] * 5
                Usuario.objects.update(vidas = 6)
                print("passou")

            for contador,letras_certas in enumerate(list(resposta)):
                if letras_certas == conjuntoDeLetras[contador]:
                    letras_corretas.append(letras_certas)
                else:
                    letras_corretas.append("_")
            
            for i,acertos in enumerate(letras_corretas):
                if acertos != "_":
                    palavraTermo[i] = acertos
            if perdeu == False :
                request.session['palavraTermo'] = palavraTermo
    
    
    return render(request, "polls/Jogo.html", {"informacao": informacao, 
                                                    "conjuntoDeLetras": conjuntoDeLetras,
                                                    "vidas": usuario.vidas,
                                                    "palavraTermo": palavraTermo,
                                                    "acertou":acertou,
                                                    "perdeu":perdeu,
                                                    "palavra":palavra,
                                                    })



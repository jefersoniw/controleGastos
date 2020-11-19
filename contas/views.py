from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Transacao


def home(request):
    data = {}
    data['transacoes'] = ['tt1', 'tt2', 'tt3']

    data['now'] = datetime.datetime.now()
    # html = "<html><body> Agora são %s. </body></html>" % now
    # return HttpResponse(html)

    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)
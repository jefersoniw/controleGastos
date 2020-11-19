from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Transacao
from .form import TransacaoForm


def home(request):
    data = {}
    data['transacoes'] = ['tt1', 'tt2', 'tt3']

    data['now'] = datetime.datetime.now()
    # html = "<html><body> Agora são %s. </body></html>" % now
    # return HttpResponse(html)

    return render(request, 'contas/home.html', data)


#METODOS DO CRUD
def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form

    return render(request, 'contas/form.html', data)
    #return render(request, 'contas/form.html', {'form': form})
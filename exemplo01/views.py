from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django_tables2 import SingleTableView
from .models import Pessoa
from .tables import pessoa_table


def index(request):
    usuario = request.POST.get('username')
    senha = request.POST.get('password')
    user = authenticate(username=usuario, password=senha)
    if user is not None:
        login(request, user)
        request.session['username'] = usuario
        request.session['password'] = senha
        request.session['usernamefull'] = user.get_full_name()
        print(request.session['username'])
        print(request.session['password'])
        print(request.session['usernamefull'])
        from django.shortcuts import redirect
        return redirect('menu_alias')
    else:
        return render(request, 'index.html')


def pagina0(request):
    return render(request, 'pagina0.html')


def pagina1(request):
    return render(request, 'pagina1.html')


def pagina2(request):
    dicionario = {}
    registros = Pessoa.objects.all()
    dicionario['pessoas'] = registros
    return render(request, 'pagina2.html', dicionario)


def pagina3(request):
    dicionario = {}
    registros = Pessoa.objects.all()
    dicionario['pessoas'] = registros
    return render(request, 'pagina3.html', dicionario)


def pagina4(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    celular = request.POST.get('celular')
    funcao = request.POST.get('funcao')
    nascimento = request.POST.get('nascimento')
    ativo = request.POST.get('ativo')
    print("Nome:", nome)
    print("eMail:", email)
    print("Celular:", celular)
    print("Funcao:", funcao)
    print("Nascimento:", nascimento)
    print("ativo:", ativo)
    return render(request, 'pagina4.html')


class pessoa_list(ListView):
    model = Pessoa
    template_name = 'exemplo01/pessoa_list.html'


class pessoa_menu(SingleTableView):
    model = Pessoa
    table_class = pessoa_table
    template_name = 'exemplo01/pessoa_menu.html'
    table_pagination = {"per_page": 5}


class pessoa_create(CreateView):
    model = Pessoa
    fields = ['nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']

    def get_success_url(self):
        return reverse_lazy('menu_alias')


class pessoa_update(UpdateView):
    model = Pessoa
    fields = ['nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']

    def get_success_url(self):
        return reverse_lazy('menu_alias')


class pessoa_delete(DeleteView):
    model = Pessoa
    fields = ['nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']
    template_name_suffix = '_confirm_delete'

    def get_success_url(self):
        return reverse_lazy('menu_alias')
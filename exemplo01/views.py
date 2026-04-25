from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django_tables2 import SingleTableView
from .models import Pessoa, procedimento, procedimento_executado
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


def pagina5(request):
    if not (request.user.has_perm('exemplo01.add_pessoa')):
        return HttpResponse("Sem permissão para adicionar pessoas")
    xnome = request.POST.get('nome')
    xemail = request.POST.get('email')
    xcelular = request.POST.get('celular')
    xfuncao = request.POST.get('funcao')
    xnascimento = request.POST.get('nascimento')
    xativo = request.POST.get('ativo')
    print("Nome:", xnome)
    print("eMail:", xemail)
    print("Celular:", xcelular)
    print("Funcao:", xfuncao)
    print("Nascimento:", xnascimento)
    print("ativo:", xativo)
    if xnome is not None:
        xativo = False
        if xativo == 'on':
            xativo = True
        Pessoa.objects.create(
            nome=xnome, email=xemail, celular=xcelular,
            funcao=xfuncao, nascimento=xnascimento, ativo=xativo
        )
    return render(request, 'pagina5.html')


def pagina6(request):
    dicionario = {}
    registros = Pessoa.objects.all()
    dicionario['pessoas'] = registros
    return render(request, 'pagina6.html', dicionario)


def pagina7(request):
    from datetime import date
    dicionario = {}
    registros = Pessoa.objects.all()
    dicionario['pessoas'] = registros
    dicionario['data'] = date.today()
    return render(request, 'pagina7.html', dicionario)


def pagina8(request):
    dicionario = {}
    registros = Pessoa.objects.all()
    dicionario['pessoas'] = registros
    return render(request, 'exemplo01/listar_pessoas.html', dicionario)


def pagina9(request):
    import pandas as pd
    eixo_y = []
    p = Pessoa.objects.all()
    for _regs in p:
        eixo_x = []
        eixo_x.append(_regs.id)
        eixo_x.append(_regs.nome)
        eixo_x.append(_regs.email)
        eixo_x.append(_regs.celular)
        eixo_x.append(_regs.nascimento)
        eixo_x.append(_regs.ativo)
        eixo_y.append(eixo_x)
    _rotulos_colunas = []
    _rotulos_colunas.append("id")
    _rotulos_colunas.append("nome")
    _rotulos_colunas.append("email")
    _rotulos_colunas.append("celular")
    _rotulos_colunas.append("nascimento")
    _rotulos_colunas.append("ativo")
    df = pd.DataFrame(eixo_y, columns=_rotulos_colunas)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=pessoas.csv'
    df.to_csv(path_or_buf=response)
    return response


def pagina10(request):
    import pandas as pd
    import os
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'pessoas.csv')
    df = pd.read_csv(csv_path, sep=',')
    for linha, coluna in df.iterrows():
        print(linha, "ID:", coluna['id'])
        print(linha, "Nome:", coluna['nome'])
        print(linha, "eMail:", coluna['email'])
        print(linha, "Celular:", coluna['celular'])
        print(linha, "Nascimento:", coluna['nascimento'])
        print(linha, "Ativo:", coluna['ativo'])
    return HttpResponse("Arquivo Importado")


class pessoa_list(ListView):
    model = Pessoa
    template_name = 'exemplo01/pessoa_list.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("exemplo01.view_pessoa"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para listar pessoas")


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
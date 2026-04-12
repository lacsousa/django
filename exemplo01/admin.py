from django.contrib import admin
from .models import *

@admin.action(description="Habilitar Registros Selecionados")
def habilitar_pessoas(ModelAdmin, request, queryset):
    for p in queryset:
        p.ativo = True
        p.save()

@admin.action(description="Desabilitar Registros Selecionados")
def desabilitar_pessoas(ModelAdmin, request, queryset):
    queryset.update(ativo=False)



class PessoaCustomizado(admin.ModelAdmin):
    list_display = ('nome', 'email', 'celular', 'funcao', 'calcula_idade', 'ativo' )
    actions = [habilitar_pessoas, desabilitar_pessoas]
    
    @admin.display(description='Idade')
    def calcula_idade(self, obj):
        if obj.nascimento:
            from datetime import date
            hoje = date.today()
            # Calcula a idade descontando um ano caso a pessoa ainda não tenha feito aniversário no ano atual
            idade = hoje.year - obj.nascimento.year - ((hoje.month, hoje.day) < (obj.nascimento.month, obj.nascimento.day))
            return idade
        return "-"

admin.site.register(Pessoa, PessoaCustomizado)
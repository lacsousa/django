from django.shortcuts import render
from django.http import HttpResponse
from .models import Medico, Paciente, Procedimento, Consulta

def listamedico(request):
    medicos = Medico.objects.all()
    return render(request, 'exemplo02/listamedico.html', {'medicos': medicos})


def listaPaciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'exemplo02/listaPaciente.html', {'pacientes': pacientes})


def detalheConsulta(request):
    consultas = Consulta.objects.select_related('paciente', 'medico', 'procedimento').all()
    return render(request, 'exemplo02/detalheConsulta.html', {'consultas': consultas})


def novaConsulta(request):
    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        medico_id = request.POST.get('medico')
        procedimento_id = request.POST.get('procedimento')
        data_consulta = request.POST.get('data_consulta')
        observacao = request.POST.get('observacao')

        paciente = Paciente.objects.get(id=paciente_id)
        medico = Medico.objects.get(id=medico_id)
        procedimento = Procedimento.objects.get(id=procedimento_id)

        nova_consulta = Consulta.objects.create(
            paciente=paciente,
            medico=medico,
            procedimento=procedimento,
            data_consulta=data_consulta,
            observacao=observacao
        )
        nova_consulta.save()

        return HttpResponse("Consulta criada com sucesso!")

    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()
    procedimentos = Procedimento.objects.all()

    return render(request, 'exemplo02/novaConsulta.html', {
        'pacientes': pacientes,
        'medicos': medicos,
        'procedimentos': procedimentos
    })
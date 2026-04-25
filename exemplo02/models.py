from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    especialidade = models.CharField(max_length=50, null=True, blank=True, verbose_name='Especialidade')
    crm = models.CharField(max_length=20, null=False, blank=False, verbose_name='CRM')
    telefone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefone')
    email = models.EmailField(max_length=50, null=True, blank=True, verbose_name='E-mail')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Paciente(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    cpf = models.CharField(max_length=20, null=False, blank=False, verbose_name='CPF')
    telefone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefone')
    email = models.EmailField(max_length=50, null=True, blank=True, verbose_name='E-mail')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Procedimento(models.Model):
    descricao = models.CharField(max_length=50, null=False, blank=False, verbose_name='Descrição')
    codigo = models.CharField(max_length=20, null=False, blank=False, verbose_name='Código')
    valor = models.FloatField(null=True, blank=True, default=None, verbose_name='Valor')

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name='Paciente')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name='Médico')
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE, verbose_name='Procedimento')
    data_consulta = models.DateTimeField(null=False, blank=False, verbose_name='Data da Consulta')
    Observacao = models.CharField(max_length=200, null=True, blank=True, verbose_name='Observação')

    def __str__(self):
        return f"{self.paciente.nome} - {self.medico.nome}"

    class Meta:
        ordering = ['-data_consulta']
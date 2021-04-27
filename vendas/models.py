from django.db import models


# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    marca = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.nome + '. R$: ' + str(self.valor)


class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    email_cliente = models.EmailField(blank=True, null=True, verbose_name='E-mail')

    def __str__(self):
        return self.nome


class Fornecedore(models.Model):
    fornecedor = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Fornecedor')
    cnpj = models.CharField(max_length=11, blank=False, null=False, verbose_name='CNPJ')
    email_fornecedor = models.EmailField(blank=True, null=True, verbose_name='E-mail')

    def __str__(self):
        return self.fornecedor


class Venda(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome da Venda')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False,
                                verbose_name='Valor total da venda')
    data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False)
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)

    def __str__(self):
        return str(self.pk) + ' - ' + self.nome


class Funcionário(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    matricula = models.CharField(max_length=255, blank=False, null=False, verbose_name='Matricula')
    email_cliente = models.EmailField(blank=True, null=True, verbose_name='E-mail')

    def __str__(self):
        return self.nome





from django.db import models


# Create your models here.
class Cadastro(models.Model):
    date = models.DateField()
    produto = models.CharField(max_length=50)
    solicitante = models.CharField(max_length=50)
    seguradora = models.CharField(max_length=50)
    carro_rebocado = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)
    sinistro = models.CharField(max_length=10)
    tot_km = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    condutor = models.CharField(max_length=50)
    destino_inicial = models.CharField(max_length=150)
    destino_final = models.CharField(max_length=150)
    observacoes = models.CharField(max_length=350, null=True, blank=True)






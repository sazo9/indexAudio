from django.db import models


class Empresas(models.Model):
    empresa = models.CharField(max_length=200)


class Audios(models.Model):
    idx = models.IntegerField(default=0)
    nome = models.CharField(max_length=200)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Data Criacao')
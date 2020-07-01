﻿from django.db import models


# Create your models here.
class Categoria(models.Model):
    dt_criacao = models.DateTimeField()
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome
    
        
class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7,decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True,blank=True)   
    
    def __str__(self):
            return self.descricao        
    
    class Meta:
        verbose_name_plural = 'Transações'
        


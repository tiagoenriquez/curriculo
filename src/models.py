from django.db import models


class Contato(models.Model):
    chave_em_portugues = models.CharField(max_length=15)
    chave_em_ingles = models.CharField(max_length=15)
    valor = models.CharField(max_length=123)

    def __str__(self):
        return f"{self.chave_em_portugues}: {self.valor}"
    
    class Meta:
        ordering = ['id']


class Competencia(models.Model):
    nome = models.CharField(max_length=63)
    nota = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['-nota']


class Experiencia(models.Model):
    empresa = models.CharField(max_length=127)
    cargo_em_portugues = models.CharField(max_length=127)
    cargo_em_ingles = models.CharField(max_length=127)
    inicio = models.DateField()
    fim = models.DateField(null=True, blank=True)

    def __str__(self):
        experiencia = self.empresa
        experiencia += f": {self.cargo_em_portugues}"
        experiencia += f", de {self.inicio.strftime('%d/%m/%Y') if self.inicio else '?'}"
        experiencia += f" até {self.fim.strftime('%d/%m/%Y') if self.fim else '?'}"
        return experiencia
    
    class Meta:
        ordering = ['-inicio']


class Resumo(models.Model):
    em_portugues = models.TextField()
    em_ingles = models.TextField()

    def __str__(self):
        return self.em_portugues

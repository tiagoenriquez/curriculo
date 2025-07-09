from django.contrib import admin
from .models import Contato, Competencia, Experiencia, Resumo


admin.site.register([Contato, Competencia, Experiencia, Resumo])

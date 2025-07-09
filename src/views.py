from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from src.models import Competencia, Contato, Experiencia, Resumo


def perguntar(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'src/perguntas.html')
    elif request.method == "POST":
        n_competencias = int(request.POST.get("n_competencias", 5))
        idioma = request.POST.get("idioma")
        contatos = Contato.objects.all()
        competencias = Competencia.objects.all()[:n_competencias]
        resumo = Resumo.objects.first()
        experiencias = Experiencia.objects.all()
        template = "src/curriculo_pt.html" if idioma == "portugues" else "src/curriculo_en.html"
        context = {"contatos": contatos, "competencias": competencias, "resumo": resumo, "experiencias": experiencias}
        return render(request, template, context)
    else:
        return HttpResponse("<h1>Método inválido</h1>", status=405)

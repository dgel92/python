from django.http import HttpResponse
from django.shortcuts import render
def saludo(request):
    return HttpResponse("hola Djando-coder")

def saludo_plantilla(request):
    contexto = {}
    return render(request, "index.html", contexto)
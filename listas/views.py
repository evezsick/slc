from django.shortcuts import render, HttpResponse
from .models import Evento, SLC, Lista

def index(request):
	return render(request, "listas/index.html", {
    	"listas": SLC.objects.all()
	})

def Lista(request):
	Listas = Lista.objects.get(id=nome_id)
	return render(request, "listas/event.html", {
    	"Listas": Lista.objects.all()
	})

def Evento(request, produto_id):
	Eventos = Evento.objects.get(id=produto_id)
	return render(request, "listas/event.html", {
    	"Eventos": Evento.objects.all()
	})

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import lista

def index(request):	
	template = loader.get_template('lista/home.html')
	query_results = lista.objects.all()
	context = {'query_results':query_results}
	return HttpResponse(template.render(context, request))

def perfil(request):	
	template = loader.get_template('lista/perfil.html')
	context = {}
	return HttpResponse(template.render(context, request))

def torneo(request):	
	template = loader.get_template('lista/torneo.html')
	context = {}
	return HttpResponse(template.render(context, request))		
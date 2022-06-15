from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from main.models import *

class HomePage(TemplateView):
    template_name = 'main/homepage.html'

class PlazaList(ListView):
    model = Plaza

class KorisnikList(ListView):
    model = Korisnik

class PloviloList(ListView):
    model = Plovilo

    def get_queryset(self):
        queryset = Plovilo.objects.filter(model__startswith='E')
        return queryset

class PoPlazi(ListView):
    template_name = 'main/poplazi_list.html'
    def get_queryset(self):
        queryset = Korisnik.objects.filter(plaza = self.kwargs['pk'])
        return queryset

class SlobodnaPlovila(ListView):
    
    def get_queryset(self):
        queryset = Plovilo.objects.filter(iznajmljen = False)
        return queryset
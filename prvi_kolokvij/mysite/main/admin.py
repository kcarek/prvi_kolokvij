from django.contrib import admin
from main.models import *

lista = [Plaza, Korisnik, Plovilo]
admin.site.register(lista)
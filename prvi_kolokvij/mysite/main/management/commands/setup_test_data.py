import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factories import *

NUM_PLAZA = 50
NUM_KORISNIK = 300
NUM_PLOVILO = 500

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Plaza, Korisnik, Plovilo]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_PLAZA):
            plaza = PlazaFactory()

        for _ in range(NUM_KORISNIK):
            korisnik = KorisnikFactory()

        for _ in range(NUM_PLOVILO):
            plovilo = PloviloFactory()

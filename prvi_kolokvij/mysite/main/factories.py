import factory
from factory.django import DjangoModelFactory
import factory.fuzzy
from main.models import *

## Defining a factory
class PlazaFactory(DjangoModelFactory):
    class Meta:
        model = Plaza

    naziv = factory.Faker("first_name")
    opis = factory.Faker("sentence", nb_words=100)
    


class KorisnikFactory(DjangoModelFactory):
    class Meta:
        model = Korisnik

    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    email = factory.Faker("email")
    plaza = factory.Iterator(Plaza.objects.all())



class PloviloFactory(DjangoModelFactory):
    class Meta:
        model = Plovilo

    proizvodac = factory.Faker("first_name")
    model = factory.Faker("last_name")
    godina_proizvodnje = factory.fuzzy.FuzzyInteger(0, 100)
    iznajmljen = factory.Faker('boolean')
    korisnik = factory.Iterator(Korisnik.objects.all())
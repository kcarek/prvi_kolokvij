from django.db import models as m

# Create your models here.


class Plaza(m.Model):
    naziv = m.CharField(max_length=100)
    opis = m.TextField()

    def __str__(self):
        return self.naziv

class Korisnik(m.Model):
    ime = m.CharField(max_length=100)
    prezime = m.CharField(max_length=100)
    email = m.EmailField()
    plaza = m.ForeignKey(Plaza, on_delete=m.CASCADE, null=True)

    def __str__(self):
        return self.ime

class Plovilo(m.Model):
    proizvodac = m.CharField(max_length=100)
    model = m.CharField(max_length=100)
    godina_proizvodnje = m.IntegerField()
    iznajmljen = m.BooleanField(default=False)
    korisnik = m.ForeignKey(Korisnik, on_delete=m.CASCADE, null=True)

    def __str__(self):
        return self.korisnik
from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('plaza', views.PlazaList.as_view(), name='plazalist'),
    path('korisnik', views.KorisnikList.as_view(), name='korisniklist'),
    path('plovilo', views.PloviloList.as_view(), name='plovilolist'),
    path('plaza/<int:pk>', views.PoPlazi.as_view(), name='poplazi'),
    path('slobodna', views.SlobodnaPlovila.as_view(), name='slobodnaplovila'),
]
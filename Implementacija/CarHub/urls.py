from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name="CarHub"

urlpatterns = [

    path('pocetnaStrana', views.pocetnaStrana, name='pocetnaStrana'),
    path('postavljanjeOglasa', views.postavljanjeOglasa),
    path('profilKorisnika', views.profilKorisnika),
    path('profilDrugogKorisnika', views.profilDrugogKorisnika),
    path('urediProfil', views.urediProfil),
    path('boostOglasa/<int:oglas_id>',views.BoostOglasa),
    path('profilDrugogKorisnika/<int:korisnik_id>', views.profilDrugogKorisnika, name='profilDrugogKorisnika'),
    path('pretragaOglasa', views.PretragaOglasa),
    path('cet/<int:idKor>', views.cet, name='cet'),
    path('pretragaOglasaRent', views.PretragaOglasaRent),
    path('urediProfil', views.urediProfil),
    path('',views.pocetnaStrana),
    path('prijava',views.prijava),
    path('registracija',views.registracija),
    path('logout',views.logout,name="logout"),
    path('postavljanjeOglasa', views.postavljanjeOglasa),
    path('konkretanOglasProdaja/<int:oglas_id>',views.konkretanOglasProdaja),
    path('konkretanOglasRent/<int:oglas_id>',views.konkretanOglasRent)


]
if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this
from .models import *
from json import dumps

# from CarHub.forms import NewUserForm


# Create your views here.


def Test(request):
    # return HttpResponse("<h1> CarHub doktoriii</h1>")
    return render(request, 'pocetnaStrana.html', {'imeSlike': 'carhublogo.png'})


def Ulogovan(request):
    # return HttpResponse("<h1> CarHub doktoriii</h1>")
    return render(request, 'pocetnaStranaUlogovan.html')

@login_required(login_url='prijava.html')
def profilKorisnika(request):
    return render(request, 'profilKorisnika.html')

@login_required(login_url='prijava.html')
def urediProfil(request):
    trenutniKorisnik = request.user
    kime = None
    pas = None
    fon = None
    mail = None
    form = PromeniSliku(request.POST, request.FILES or None)
    if form.is_valid():
        kime = request.POST['ime1']
        pas = request.POST['sifra1']
        fon = request.POST.get('telefon1')
        mail = request.POST.get('mejl1')
        slika = form.cleaned_data.get('slika')
        trenutniKorisnik.slika = slika
        if len(kime)> 6 :
            trenutniKorisnik.username = kime
        if len(pas) > 6 :
            trenutniKorisnik.set_password(pas)
        if len(fon)> 6 :
            trenutniKorisnik.kontakt_telefon = fon
        if len(mail)> 6 :
            trenutniKorisnik.email = mail
        trenutniKorisnik.save()
    context = {
        "forma_promenaSlike": form
    }


    return render(request, 'urediProfil.html',context = context)


@login_required(login_url='prijava.html')
def postavljanjeOglasa(request):
    form=PostavljanjeOglasa(request.POST or None,request.FILES or None)
    if form.is_valid():
        izbor = request.POST['izbor']
        brend = request.POST['dropdown_Brend']
        naziv_model = request.POST['dropdown_Model']
        godiste = form.cleaned_data.get('godiste')
        kilometraza = form.cleaned_data.get('kilometraza')
        snaga = form.cleaned_data.get('snagaMotora')
        karoserija = form.cleaned_data.get('karoserija')
        slike = form.cleaned_data.get('slike')

        model_id = Model.objects.filter(godisteOd__lte=godiste).filter(godisteDo__gte=godiste).filter(
            brend=brend).filter(naziv_modela=naziv_model)  #filtriranje radi pronalaska id-ja modela
        print(model_id)
        #proveriti sta vraca post request za izbor (da li vraca value od pritisnitog dugmeta)
        if (izbor == "prodaja"):
            cena = request.POST["cenaProdaja"];

            model = Oglas(tip = "p", cena = cena, boost = 0, grad = '', slike = slike,
                          snaga = snaga, kilometraza=kilometraza, karoserija=karoserija,
                          godiste=godiste, model_idmodel=model_id.first())
            model.save()
        else:
            pass
        #napraviti razlicite ifove za prodaju i iznajmljivanje
        #ako je prodaja, moze odmag da se postavi oglas
        #ako je iznajmljivanje, treba smisliti nacin za kupljenje datuma i za njihovubacivanje u bazu
        #takodje, mora se naci id_Modela pomocu brenda, modela i godista

    brendovi = Model.objects.values("brend").distinct()
    brendovi_modeli = list(Model.objects.values("brend", "naziv_modela"))
    niz = []
    for model in brendovi_modeli:
        niz.append([str(model["brend"]), str(model["naziv_modela"])])
    # print(niz)
    # print(brendovi_modeli)

    dataJSON = dumps(niz)
    context = {
        "data": dataJSON,
        "brendovi" : brendovi,
        "forma_postaviOglas":form
    }
    return render(request=request, template_name='testForme.html', context = context)


def registracija(request):
    form = KorisnikNoviForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("CarHub:pocetnaStranaUlogovan")

    form = KorisnikNoviForm()
    return render(request=request, template_name="registracijaProbaDjango.html", context={"register_form": form})
    # return render(request,"registracijaProbaDjango.html")

def pretragaOglasa(request):
    return render(request, 'pretragaOglasa.html')

def pregledOglasa(request):
    return render(request, 'pregledOglasa.html')


def prijava(request):
     if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) #moraju da se taguju
            if user is not None:
                login(request, user)
                messages.info(request, f"Ulogovani ste kao{username}.")
                return redirect("CarHub:pocetnaStranaUlogovan")
            else:
                messages.error(request, "Netacno ime ili lozinka.")
        else:
             messages.error(request, "Netacno ime ili lozinka.")
     form = AuthenticationForm()
     return render(request=request, template_name="prijavaProbaDjango.html", context={"login_form": form})


def logout(request):
    messages.info(request, "Uspesno ste izlogovani")
    return redirect("CarHub:pocetnaStrana")



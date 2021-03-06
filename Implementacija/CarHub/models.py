import datetime

from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.


class Korisnik(AbstractUser):
    kontakt_telefon = models.CharField(db_column='Kontakt telefon',
                                       max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slika = models.FileField(db_column='Slika', upload_to='imgs/', null=True, blank=True,
                             default='imgs/default.jpg')  # Field name made lowercase.
    uloga = models.CharField(db_column='Uloga', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'korisnik'


class Model(models.Model):
    idmodel = models.AutoField(db_column='idModel', primary_key=True)  # Field name made lowercase.
    carreviewlink = models.CharField(db_column='CarReviewLink', max_length=500, blank=True,
                                     null=True)  # Field name made lowercase.
    brend = models.CharField(db_column='Brend', max_length=100)  # Field name made lowercase.

    naziv_modela = models.CharField(db_column='Naziv modela',
                                    max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    godisteOd = models.IntegerField(db_column='GodisteOd', default=0)  # modeli su se pravili od nekog godista do drugog
    godisteDo = models.IntegerField(db_column='GodisteDo', default=0)

    class Meta:
        db_table = 'model'


class Oglas(models.Model):
    idoglas = models.AutoField(db_column='idOglas', primary_key=True)  # Field name made lowercase.
    tip = models.CharField(db_column='Tip', max_length=1)  # Field name made lowercase.
    cena = models.IntegerField(db_column='Cena', blank=True, null=True)  # Field name made lowercase.
    boost = models.IntegerField(db_column='Boost', blank=True, null=True)  # Field name made lowercase.
    grad = models.CharField(db_column='Grad', max_length=45)  # Field name made lowercase
    opis = models.TextField(db_column='Opis')
    snaga = models.IntegerField(db_column='Snaga', default=0)
    kilometraza = models.IntegerField(db_column='Kilometraza', default=0)
    godiste = models.IntegerField(db_column='Godiste', default=0)
    karoserija = models.CharField(db_column="Karoserija", max_length=20, null=False, blank=True, default="limuzina")
    model_idmodel = models.ForeignKey(Model, on_delete=models.CASCADE,
                                      db_column='Model_idModel')  # Field name made lowercase.
    vlasnik_id = models.ForeignKey(Korisnik, on_delete=models.CASCADE, db_column='vlasnik_auta', related_name='vlasnik')

    class Meta:
        db_table = 'oglas'


class Slike(models.Model):
    idSlike = models.AutoField(db_column='idSlike', primary_key=True)
    slike = models.FileField(db_column='Slike', upload_to='imgs/', null=True)
    fk_oglas = models.ForeignKey(Oglas, on_delete=models.CASCADE, db_column='fk_Oglas')

    class Meta:
        db_table = 'slike'


class Datumi(models.Model):
    datumOd = models.DateField()
    datumDo = models.DateField()
    fk_oglas = models.ForeignKey(Oglas, on_delete=models.CASCADE, db_column='fk_Oglas')


class Ocena(models.Model):
    ocena = models.IntegerField(db_column='ocena')
    korisnik = models.ForeignKey(Korisnik, on_delete=models.CASCADE, db_column='korisnik', related_name='korisnik')
    ocenio = models.ForeignKey(Korisnik, on_delete=models.CASCADE, db_column='ocenio', related_name='ocenio')

    class Meta:
        db_table = 'ocena'


class Cet(models.Model):
    idCet = models.AutoField(db_column='idCet', primary_key=True)  # Field name made lowercase.
    idkorisnika1 = models.ForeignKey(Korisnik, on_delete=models.CASCADE, db_column='idKorisnika1',
                                     related_name='idkorisnika1')
    idkorisnika2 = models.ForeignKey(Korisnik, on_delete=models.CASCADE, db_column='idKorisnika2',
                                     related_name='idkorisnika2')
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    ne_procitano_Korisnik_1 = models.CharField(db_column='ne_procitano_Korisnik_1', max_length=1)
    ne_procitano_Korisnik_2 = models.CharField(db_column='ne_procitano_Korisnik_2', max_length=1)

    class Meta:
        db_table = 'cet'


class Komentar(models.Model):
    idkomentar = models.AutoField(db_column='idKomentar', primary_key=True)
    sadrzaj = models.CharField(max_length=300)
    autor = models.ForeignKey(Korisnik, on_delete=models.CASCADE, db_column='autor', related_name='autor')
    profilKorisnika = models.ForeignKey(Korisnik, on_delete=models.CASCADE, db_column='profilKorisnika',
                                        related_name='profilKorisnika')
    timestamp = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'komentar'


class SacuvaniOglasi(models.Model):
    idsacuvanioglasi = models.AutoField(db_column='idSacuvaniOglasi', primary_key=True)
    korisnik_id = models.ForeignKey(Korisnik, on_delete=models.CASCADE, db_column='korisnik', related_name='korisnik_s')
    oglas_id = models.ForeignKey(Oglas, on_delete=models.CASCADE, db_column='oglas_id', related_name='oglas_id_s')

    class Meta:
        db_table = 'sacuvanioglasi'


class MojiOglasi(models.Model):
    idmojioglasi = models.AutoField(db_column='idMojiOglasi', primary_key=True)
    korisnik_id = models.ForeignKey(Korisnik, on_delete=models.CASCADE, db_column='korisnik', related_name='korisnik_m')
    oglas_id = models.ForeignKey(Oglas, on_delete=models.CASCADE, db_column='oglas_id', related_name='oglas_id_m')

    class Meta:
        db_table = 'mojioglasi'


class Poruke(models.Model):
    idporuke = models.AutoField(db_column='idPoruke', primary_key=True)
    sadrzaj = models.CharField(db_column='Poruka', max_length=500, blank=True, null=True)
    cet_idcet = models.ForeignKey(Cet, on_delete=models.CASCADE, db_column='Cet_idCet')
    idKorisnikaPoslao = models.ForeignKey(Korisnik, on_delete=models.CASCADE, db_column='Korisnik_idKorisnika')
    timestamp = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'poruke'

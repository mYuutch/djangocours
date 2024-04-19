from django.db import models

# Create your models here.


class Acteur(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    def __str__(self):
        return self.nom + " " + self.prenom
    
class Realisateur(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    def __str__(self):
        return self.nom + " " + self.prenom
    

class MovieCard(models.Model):
    titre = models.CharField(max_length=250)
    date_sortie = models.DateField()
    realisateur = models.ForeignKey(Realisateur, on_delete=models.CASCADE,related_name='films')
    acteur = models. ManyToManyField(Acteur,related_name='films')
    avis = models.TextField()
    pub = models.BooleanField(default = False)
    note = models.IntegerField(default = 0)
    def __str__(self):
        return self.titre
    


    


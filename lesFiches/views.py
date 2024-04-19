from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from lesFiches.models import MovieCard, Acteur, Realisateur
from django.forms import ModelForm
from django.contrib import messages

class MovieCardForm(ModelForm):
    class Meta:
        model = MovieCard
        fields = ['titre','avis','date_sortie','realisateur', 'acteur', 'note']


def home(request):
    films = MovieCard.objects.all().order_by('titre')
    acteurs = Acteur.objects.all().order_by('nom')
    realisateurs = Realisateur.objects.all().order_by('nom') 
    return render(request,template_name='home.html',context={'films':films,'acteurs':acteurs,'realisateurs':realisateurs})

def realisateurs(request):
    realisateurs = Realisateur.objects.all().order_by('nom')
    return render(request,template_name='realisateurs.html',context={'realisateurs':realisateurs})


def acteurs(request):
    acteurs = Acteur.objects.all().order_by('nom')
    return render(request,template_name='acteurs.html',context={'acteurs':acteurs})

def films(request):
    films = MovieCard.objects.all().order_by('date_sortie')
    return render(request,template_name='list2.html',context={'films':films})


def formu(request):
    avis_form = MovieCardForm()
    if request.method == 'POST':
        form = MovieCardForm(request.POST)
        if form.is_valid():
            new_movie = form.save()
            messages.success(request, 'Nouveau Film' +new_movie.titre)
            context = {'film': new_movie}
            return render(request, 'details.html', context)
    return render(request, 'formulaire.html', {'avis_form': avis_form})

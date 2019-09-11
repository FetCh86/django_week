from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.

def date_actuelle(request):
    return render(request, 'blog/date.html', {'pseudo' : 'Assia', 'sexe':'Femme', 'age':33, 'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    return render(request, 'blog/addition.html', locals())


def home(request):
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes, c'est de la bombe !</p>
    """)


def view_article(request, id_article):
    if id_article > 100:
        raise Http404

    return redirect(view_redirection)


def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")


def list_articles(request, year, month=1):
    return HttpResponse('Articles de %s/%s' % (month, year))

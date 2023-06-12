from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generateur/home.html')

def motDePasse(request):
    caracteres = list("abcdefghijklmnopqrstuvwxyz")
    longueur = int(request.GET.get('longueur'))
    if request.GET.get('majuscule'):
        caracteres.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('nombre'):
        caracteres.extend(list("0123456789"))
    if request.GET.get('special'):
        caracteres.extend('&-_;:§/,#~@$*%')
    motdepasse = ""
    for i in range(longueur):
        motdepasse += random.choice(caracteres)
    return render(request, 'generateur/motdepasse.html', {"motdepasse": motdepasse})

def apropos(request):
    return render(request, "generateur/apropos.html")
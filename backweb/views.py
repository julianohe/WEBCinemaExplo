from django.http import HttpResponse
from django.shortcuts import render

""" 
Agora vamos adicionar mais algumas visualizações ao . Essas visões são um
pouco diferente, porque eles aceitam um argumento: backend/views.py

"""

def ViewsFilme(Filme):
    return HttpResponse("ola, Filme %s", Filme)


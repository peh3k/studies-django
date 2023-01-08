from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_fake
# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_fake() for _ in range(10)],
    })

def receita(request, id):
    return render(request, 'recipes/pages/receita-view.html', context= {
        'recipe': make_fake()
    })


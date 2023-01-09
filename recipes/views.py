from django.shortcuts import render
from django.http import HttpResponse
from utils.scripts.fake_gen import fake_gen
# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [fake_gen() for _ in range(10)],
    })

def receita(request, id):
    return render(request, 'recipes/pages/receita-view.html', context= {
        'card': fake_gen(),
        'page_detail': True,
    })


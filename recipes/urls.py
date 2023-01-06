from django.urls import path
from recipes.views import index, contato


urlpatterns = [
    path('lab/', index),
    path('contato/', contato)
]

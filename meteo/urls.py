from django.urls import path
from . import views

app_name = "meteo"

urlpatterns = [


    path('previsao/', views.cidades, name='previsao'),


]

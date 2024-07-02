from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from datetime import date
import requests

class CityForm(forms.Form):
    idCidade = forms.ChoiceField(label='Cidade', choices=[], required=True)

def cidades(request):
    url_previsao_base = "http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/"
    url_classes_tempo = "http://api.ipma.pt/open-data/weather-type-classe.json"
    url_cidades = "https://api.ipma.pt/open-data/distrits-islands.json"

    resposta_cidades = requests.get(url_cidades)
    dados_cidades = None
    cidades = {}
    if resposta_cidades.status_code == 200:
        dados_cidades = resposta_cidades.json()
        if dados_cidades and 'data' in dados_cidades and len(dados_cidades['data']) > 0:
            for cidade in dados_cidades['data']:
                id = cidade.get('globalIdLocal')
                nome = cidade.get('local')
                cidades[id] = nome

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.fields['idCidade'].choices = [(id, nome) for id, nome in cidades.items()]
        if form.is_valid():
            idCidade = form.cleaned_data.get('idCidade')
            url_previsao = url_previsao_base + str(idCidade) + ".json"
        else:
            return HttpResponse("Invalid form submission.")
    else:
        form = CityForm()
        form.fields['idCidade'].choices = [(id, nome) for id, nome in cidades.items()]
        url_previsao = url_previsao_base + "1110600.json"  # Lisbon default

    resposta_previsao = requests.get(url_previsao)
    resposta_classes = requests.get(url_classes_tempo)

    dados_previsao = None
    dados_classes = None
    contexto = {}

    if resposta_previsao.status_code == 200:
        dados_previsao = resposta_previsao.json()

    if resposta_classes.status_code == 200:
        dados_classes = resposta_classes.json()

    if dados_previsao and 'data' in dados_previsao and len(dados_previsao['data']) > 0:


        nome_cidade = cidades[dados_previsao['globalIdLocal']]


        previsao_hoje = dados_previsao['data'][0]
        id_weather_type = previsao_hoje.get('idWeatherType', None)
        descricao_tempo = 'Não foi possível obter a previsão do tempo.'

        if id_weather_type and dados_classes:
            for dado in dados_classes['data']:
                if id_weather_type == dado.get('idWeatherType', None):
                    descricao_tempo = dado.get('descWeatherTypePT')

        padded_number = str(id_weather_type).zfill(2) if id_weather_type else None
        icon_url = f"/static/meteo/w_ic_d_{padded_number}anim.svg" if id_weather_type else None

    previsoes = []
    for previsao in dados_previsao['data'][1:5]:
        id_weather_type = previsao.get('idWeatherType', None)
        padded_number = str(id_weather_type).zfill(2) if id_weather_type else None
        icon_url = f"/static/meteo/w_ic_d_{padded_number}anim.svg" if id_weather_type else None

        descricao_tempo = 'Não foi possível obter a previsão do tempo.'
        for dado in dados_classes['data']:
            if id_weather_type == dado.get('idWeatherType', None):
                descricao_tempo = dado.get('descWeatherTypePT')

        previsoes.append({
            'data': previsao.get('forecastDate'),
            'temperatura_minima': previsao.get('tMin', 'N/A'),
            'temperatura_maxima': previsao.get('tMax', 'N/A'),
            'descricao_tempo': descricao_tempo,
            'icon_url': icon_url
        })


        contexto = {
            'cidade': nome_cidade,
            'temperatura_minima': previsao_hoje.get('tMin', 'N/A'),
            'temperatura_maxima': previsao_hoje.get('tMax', 'N/A'),
            'data': date.today().strftime('%d/%m/%Y'),
            'descricao_tempo': descricao_tempo,
            'iconUrl': icon_url,
            'cidades': cidades,
            'form': form,
            'previsoes': previsoes,
        }

    return render(request, 'meteo/todayLisbon.html', contexto)
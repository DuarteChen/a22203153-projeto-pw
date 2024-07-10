from django.urls import path
from .views import *

app_name = "bands"


urlpatterns = [
    path('', band_list, name='band_list'),

    path('recurso/', band_list_recurso, name='band_list_recurso'),

    path('musics/json/', musicsJson, name='musicsJson'),

    path('<int:band_id>/', band_detail, name='band_detail'),

    path('add_band/', add_band, name='add_band_form'),
    path('<int:band_id>/add_album/', add_album, name='add_album_form'),

    path('album/<int:album_id>/', album_detail, name='album_detail'),

    path('album/<int:album_id>/add_music/', add_music, name='add_music'),

    path('music/<int:music_id>/', music_detail, name='music_detail'),
]

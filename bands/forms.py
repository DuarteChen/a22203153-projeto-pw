from django import forms
from .models import *

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['band_name', 'start_date', 'description', 'music_type', 'band_image']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'album_release_date', 'band']

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['music_name', 'release_date', 'lyrics']



from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from .forms import *





'''
Função geral para rederização de todas as páginas ------------------------------
'''
def contextFun(request):
    username = request.user.username if request.user.is_authenticated else 'Guest'

    context = {
        'anoAtual' : datetime.today().year,
        'username': username
    }

    return context

'''
Bands views --------------------------------------------------------------------
'''

def band_list(request):
    bands = Band.objects.all()

    context = contextFun(request)
    context['bands'] = bands
    return render(request, 'bands/band_list.html', context)


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)

    context = contextFun(request)
    context['band'] = band
    return render(request, 'bands/band_detail.html', context)




def add_band(request):
    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bands:band_list')
    else:
        form = BandForm()

    context = contextFun(request)
    context['form'] = form

    return render(request, 'bands/add_band.html', context)


def add_album(request, band_id):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bands:band_detail', band_id=band_id)
    else:
        form = AlbumForm(initial={'band': band_id})

    context = contextFun(request)
    context['form'] = form
    return render(request, 'bands/add_album.html', context)


def album_detail(request, album_id):

    album = Album.objects.get(pk=album_id)


    context = contextFun(request)
    context['album'] = album

    return render(request, 'bands/album_detail.html', context)

def add_music(request, album_id):
    album = Album.objects.get(pk=album_id)

    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            music_name = form.cleaned_data['music_name']
            release_date = form.cleaned_data['release_date']
            lyrics = form.cleaned_data['lyrics']


            new_music = Music.objects.create(
                music_name=music_name,
                release_date=release_date,
                lyrics=lyrics,
            )


            album.musics.add(new_music)
            album.save()


            return redirect('bands:album_detail', album_id=album_id)
    else:
        form = MusicForm()

    context = contextFun(request)
    context['form'] = form
    context['album_id'] = album_id

    return render(request, 'bands/add_music.html', context)


def music_detail(request, music_id):
    music = Music.objects.get(pk=music_id)

    context = contextFun(request)
    context['music'] = music

    return render(request, 'bands/music_detail.html', context)












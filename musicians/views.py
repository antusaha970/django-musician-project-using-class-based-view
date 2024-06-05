from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .form import MusiciansForm, AlbumsForm
from .models import Album, Musician
# Create your views here.


class AddMusiciansView(CreateView):
    model = Musician
    form_class = MusiciansForm()
    template_name = 'addMusicians.html'
    success_url = reverse_lazy("view_musics")


def add_musicians(request):
    if request.method == 'POST':
        form = MusiciansForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_musics")
    else:
        form = MusiciansForm()

    return render(request, 'addMusicians.html', {'form': form})


def add_album(request):
    if request.method == 'POST':
        form = AlbumsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_musics")
    else:
        form = AlbumsForm()

    return render(request, 'addAlbums.html', {'form': form})


def view_musics(request):
    data = Album.objects.all()
    return render(request, 'viewMusics.html', {'data': data})


def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect("view_musics")


def edit_album(request, id):
    album = Album.objects.get(pk=id)
    form = AlbumsForm(instance=album)
    if request.method == 'POST':
        form = AlbumsForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("view_musics")
    return render(request, 'addAlbums.html', {'form': form})


def edit_musicians(request, id):
    musician = Musician.objects.get(pk=id)
    form = MusiciansForm(instance=musician)
    if request.method == 'POST':
        form = MusiciansForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect("view_musics")

    return render(request, 'editMusicians.html', {'form': form})

from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .form import MusiciansForm, AlbumsForm
from .models import Album, Musician
# Create your views here.


class AddMusiciansView(CreateView):
    model = Musician
    form_class = MusiciansForm
    template_name = 'addMusicians.html'
    success_url = reverse_lazy("view_musics")


class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumsForm
    template_name = "addAlbums.html"
    success_url = reverse_lazy("view_musics")


class DisplayMusicsView(ListView):
    model = Album
    template_name = 'viewMusics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = context['object_list']
        return context


class DeleteAlbumView(DeleteView):
    model = Album
    success_url = reverse_lazy("view_musics")
    pk_url_kwarg = 'id'


class UpdateAlbumView(UpdateView):
    model = Album
    form_class = AlbumsForm
    pk_url_kwarg = 'id'
    template_name = 'addAlbums.html'
    success_url = reverse_lazy("view_musics")


class UpdateMusicsView(UpdateView):
    model = Musician
    form_class = MusiciansForm
    pk_url_kwarg = 'id'
    template_name = 'editMusicians.html'
    success_url = reverse_lazy("view_musics")

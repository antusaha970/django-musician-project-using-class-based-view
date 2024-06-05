from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_musicians, name="add_musicians"),
    path('delete/album/<int:id>', views.delete_album, name="delete_album"),
    path('edit/album/<int:id>', views.edit_album, name="edit_album"),
    path('edit/musician/<int:id>', views.edit_musicians, name="edit_musician"),
    path('add/album/', views.add_album, name="add_album"),
    path('view-musics/', views.view_musics, name="view_musics"),
]

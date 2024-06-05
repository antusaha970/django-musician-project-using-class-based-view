from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.AddMusiciansView.as_view(), name="add_musicians"),
    path('delete/album/<int:id>',
         views.DeleteAlbumView.as_view(), name="delete_album"),
    path('edit/album/<int:id>', views.UpdateAlbumView.as_view(), name="edit_album"),
    path('edit/musician/<int:id>',
         views.UpdateMusicsView.as_view(), name="edit_musician"),
    path('add/album/', views.AddAlbumView.as_view(), name="add_album"),
    path('view-musics/', views.DisplayMusicsView.as_view(), name="view_musics"),
]

from django.urls import include, path
from gallery.views import (CreatePhotoView, PhotoListView, PhotoDeleteView,
                            PhotoUpdateView, GalleryView)

app_name ='gallery'
urlpatterns = [
    path('createphoto/', CreatePhotoView, name='createphoto'),
    path('photo-list/', PhotoListView, name='photolist'),
    path('photo-delete/<int:pk>/', PhotoDeleteView, name='photodelete'),
    path('photo-update/<int:pk>/', PhotoUpdateView, name='photoupdate'),
    path('gallery/', GalleryView, name='gallery'),

]

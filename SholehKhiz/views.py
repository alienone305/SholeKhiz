from django.shortcuts import render
from gallery.models import GalleryModel

def HomeView(request):
    photos = GalleryModel.objects.all()
    return render(request,'home.html',{'photos':photos})

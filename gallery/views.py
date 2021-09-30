from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.shortcuts import get_object_or_404, get_list_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import jdatetime
import datetime
import random
from django.utils import timezone

# handmade
from gallery.models import GalleryModel
from gallery.forms import GalleryForm
from accounts.decorators import superuser_required

@login_required
@superuser_required
def CreatePhotoView(request):
    if request.method == 'POST':
        gallery_form = GalleryForm(data = request.POST)
        if gallery_form.is_valid():

             photo = gallery_form.save(commit=False)
             if 'picture' in request.FILES:
                photo.picture = request.FILES['picture']
             photo.save()
             return HttpResponseRedirect(reverse('accounts:superuserdashboard'))
        else:
            print(gallery_form.errors)
    else:
        gallery_form = GalleryForm()
    return render(request,'gallery/createphoto.html',
                  {'form':gallery_form})

@login_required
@superuser_required
def PhotoListView(request):
    try:
        photos = get_list_or_404(GalleryModel)
        return render(request,'gallery/photolist.html',
                      {'photos':photos})
    except:
        return render(request,'gallery/photolist.html')



@login_required
@superuser_required
def PhotoDeleteView(request, pk):
    photo = get_object_or_404(GalleryModel, pk = pk)
    photo.delete()
    return HttpResponseRedirect(reverse('gallery:photolist'))


@login_required
@superuser_required
def PhotoUpdateView(request,pk):
    photo = get_object_or_404(GalleryModel, pk = pk)
    photo_update_form = GalleryForm(request.POST or None, instance = photo)
    if photo_update_form.is_valid():
        photo_update_form.save()
        if 'picture' in request.FILES:
           photo.picture = request.FILES['picture']
        photo.save()
        return HttpResponseRedirect(reverse('gallery:photolist'))
    return render(request,'gallery/photoupdate.html',
                          {'form':photo_update_form,
                          'photo':photo})


def GalleryView(request):
    try:
        photos = get_list_or_404(GalleryModel)
        return render(request,'gallery/gallery.html',
                      {'photos':photos})
    except:
        return render(request,'gallery/gallery.html')

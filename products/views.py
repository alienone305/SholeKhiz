from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.forms import modelformset_factory
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404
# handmade

from products.forms import ProductsForm
from products.models import ProductsModel
from accounts.decorators import superuser_required

@login_required
@superuser_required
def CreateProductView(request):
    if request.method == 'POST':
        products_form = ProductsForm(data = request.POST)
        if products_form.is_valid():
             product = products_form.save(commit=False)
             if 'type' in request.POST:
                 type = request.POST['type']
             else:
                 type = False
             if type == "1":
                 product.is_radiator = True
             if type == "2":
                 product.is_towerdryer = True
             if type == "3":
                 product.is_package = True
             if type == "4":
                 product.is_waterheater = True

             if 'picture' in request.FILES:
                product.picture = request.FILES['picture']
             if 'cataloge' in request.FILES:
                product.cataloge = request.FILES['cataloge']
             product.save()
             return HttpResponseRedirect(reverse('accounts:superuserdashboard'))
        else:
            print(products_form.errors)
    else:
        products_form = ProductsForm()
    return render(request,'products/createproduct.html',
                  {'products_form':products_form})


@login_required
@superuser_required
def ProductsListViewSuperUser(request):
    products = ProductsModel.objects.all()
    return render(request,'products/productslistsuperuser.html',{'products':products})


@login_required
@superuser_required
def ProductsDeleteView(request, pk):
    product = get_object_or_404(ProductsModel, pk = pk)
    product.delete()
    return HttpResponseRedirect(reverse('products:listsuperuser'))


@login_required
@superuser_required
def ProductsUpdateView(request,pk):
    product = get_object_or_404(ProductsModel, pk = pk)
    product_update_form = ProductsForm(request.POST or None, instance = product)
    if product_update_form.is_valid():
        product_update_form.save()
        if 'type' in request.POST:
            type = request.POST['type']
        else:
            type = False
        if type == "1":
            product.is_radiator = True
        if type == "2":
            product.is_towerdryer = True
        if type == "3":
            product.is_package = True
        if type == "4":
            product.is_waterheater = True


        if 'picture' in request.FILES:
           product.picture = request.FILES['picture']
        if 'cataloge' in request.FILES:
           product.cataloge = request.FILES['cataloge']
        product.save()
        return HttpResponseRedirect(reverse('products:listsuperuser'))
    return render(request,'products/productupdate.html',
                          {'products_form':product_update_form,
                          'product':product,})


def TowerDryerListView(request):
    product_list = ProductsModel.objects.filter(is_towerdryer = True)
    return render(request,'products/towerdryerlist.html',{'products':product_list})


def RadiatorListView(request):
    product_list = ProductsModel.objects.filter(is_radiator = True)
    return render(request,'products/radiatorlist.html',{'products':product_list})


def PackageListView(request):
    product_list = ProductsModel.objects.filter(is_package = True)
    return render(request,'products/packagelist.html',{'products':product_list})


def WaterHeaterListView(request):
    product_list = ProductsModel.objects.filter(is_waterheater = True)
    return render(request,'products/waterheaterlist.html',{'products':product_list})

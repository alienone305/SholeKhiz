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
from django.conf import settings
from django.utils import timezone
from kavenegar import KavenegarAPI

# handmade
from products.models import ProductsModel
from order.models import OrderingModel
from order.forms import OrderingForm
from commonuser.decorators import commonuser_required
from accounts.decorators import superuser_required


@login_required
@commonuser_required
def OrderingView(request, pk):
    #api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
    product = get_object_or_404(ProductsModel, pk= pk)
    if request.method == 'POST':
        ordering_form = OrderingForm(data = request.POST)
        if ordering_form.is_valid():
             order = ordering_form.save(commit=False)
             order.user = request.user
             order.product = product
             order.save()

             return HttpResponseRedirect(reverse('home'))
        else:
            print(ordering_form.errors)
    else:
        ordering_form = OrderingForm()
    return render(request,'order/ordering.html',
                  {'ordering_form':ordering_form,'product':product})


@login_required
@superuser_required
def UnCheckedOrdersListView(request):
    order_list = OrderingModel.objects.filter(checked = False)
    return render(request,'order/uncheckedorderslist.html',{'order_list':order_list})


@login_required
@superuser_required
def CheckedOrdersListView(request):
    order_list = OrderingModel.objects.filter(checked = True)
    return render(request,'order/checkedorderslist.html',{'order_list':order_list})



@login_required
@superuser_required
def OrdersDetailView(request, pk):
    order = get_object_or_404(OrderingModel, pk = pk)
    return render(request,'order/orderdetail.html',{'order':order})

@login_required
@superuser_required
def OrdersChangeStatus(request, pk):
    order = get_object_or_404(OrderingModel, pk = pk)
    if order.checked:
        order.checked = False
    else:
        order.checked = True
    order.save()
    return render(request,'order/orderdetail.html',{'order':order})

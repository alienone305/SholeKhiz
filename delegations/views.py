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

from delegations.forms import DelegationForm
from delegations.models import DelegationModel
from accounts.decorators import superuser_required


@login_required
@superuser_required
def AddDelegationView(request):
    if request.method == 'POST':
        delegation_form = DelegationForm(data = request.POST)
        if delegation_form.is_valid():
             delegation = delegation_form.save(commit=False)
             delegation.save()
             return HttpResponseRedirect(reverse('accounts:superuserdashboard'))
        else:
            print(delegation.errors)
    else:
        delegation_form = DelegationForm()
    return render(request,'delegations/adddelegation.html',
                  {'delegation_form':delegation_form})


@login_required
@superuser_required
def DelegationsListViewSuperUser(request):
    delegations_list = DelegationModel.objects.all()
    return render(request,'delegations/delegationslistsuperuser.html',{'delegations':delegations_list})


@login_required
@superuser_required
def DelegationDeleteView(request, pk):
    delegation = get_object_or_404(DelegationModel, pk = pk)
    delegation.delete()
    return HttpResponseRedirect(reverse('delegations:listsuperuser'))


@login_required
@superuser_required
def DelegationUpdateView(request,pk):
    delegation = get_object_or_404(DelegationModel, pk = pk)
    delegation_update_form = DelegationForm(request.POST or None, instance = delegation)
    if delegation_update_form.is_valid():
        delegation_update_form.save()
        delegation.save()
        return HttpResponseRedirect(reverse('delegations:listsuperuser'))
    return render(request,'delegations/delegationupdate.html',
                          {'delegation_form':delegation_update_form,
                          'delegation':delegation,})


def DelegationsPublicList(request):
    delegations_list = DelegationModel.objects.all()
    return render(request,'delegations/delegationspubliclist.html',{'delegations':delegations_list})

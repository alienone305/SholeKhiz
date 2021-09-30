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
from django.conf import settings
from django.utils import timezone

#handmade
from accounts.forms import UserForm, UserUpdateForm
from commonuser.forms import CommonUserForm, ConfirmationForm
from accounts.models import UserModel
from commonuser.models import CommonUserModel
from commonuser.decorators import commonuser_required
from order.models import OrderingModel
from company.utils import SendMessage


def CommonUserSignupView(request):
    #api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
    try:
        last_retry_str = request.session['last_retry']
        retries = request.session['retries']
        last_retry = datetime.datetime.strptime(last_retry_str,"%Y-%m-%d %H:%M:%S")
    except:
        last_retry = datetime.datetime.now()
    now = datetime.datetime.now()
    if now >= last_retry or retries != 2:
        if request.method == 'POST':

            user_form = UserForm(data = request.POST)
            commonuser_form = CommonUserForm(data = request.POST)

            if user_form.is_valid() and commonuser_form.is_valid():
                 request.session['name'] =  user_form.cleaned_data.get('name')
                 request.session['password1'] =  user_form.cleaned_data.get('password1')
                 request.session['username'] = user_form.cleaned_data.get('username')
                 request.session['address'] = commonuser_form.cleaned_data.get('address')

                 #### generating code
                 var = '1234567890'
                 random_code=''
                 for i in range(5):
                     c = random.choice(var)
                     random_code += c
                 code = random_code
                 phone_number = '0' + user_form.cleaned_data.get('username')

                 text = 'کد فعال سازی شما: {code} \n شعله خیز آذر'.format(code = code)


                 try:
                     SendMessage(phone_number, text)
                     request.session['code'] =  code
                     now = datetime.datetime.now() + datetime.timedelta(minutes=2)
                     str_now = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
                     request.session['last_retry'] = str_now
                     try:
                         if request.session['retries'] == 1:
                             request.session['retries'] = 2
                     except:
                         request.session['retries'] = 1


                 except:
                     return HttpResponseRedirect(reverse('commonuser:wrongphonenumber'))


                 return HttpResponseRedirect(reverse('commonuser:confirm'))
            else:
                print(user_form.errors,commonuser_form.errors)


        else:
            user_form = UserForm()
            commonuser_form = CommonUserForm()

        return render(request,'commonuser/signup.html',
                              {'user_form':user_form,
                               'commonuser_form':commonuser_form})
    else:
        return HttpResponseRedirect(reverse('commonuser:twominwait'))


def UserConfirmView(request):
    name = request.session['name']
    password1 = request.session['password1']
    username = request.session['username']
    address = request.session['address']
    code = request.session['code']
    print(code)

    if request.method == 'POST':

        confirmation_form = ConfirmationForm(data = request.POST)

        if confirmation_form.is_valid():
            confirmation_code = confirmation_form.cleaned_data.get('code')
            if confirmation_code == code:
                user = UserModel.objects.create(username=username, password=password1,
                                            name = name)
                user.is_active = True
                user.is_commonuser = True
                # hashing password
                user.set_password(user.password)
                user.save()

                commonuser = CommonUserModel.objects.create(user=user, address=address,)
                commonuser.save()
                return HttpResponseRedirect(reverse('accounts:login'))
        else:
            print(confirmation_form.errors)


    else:
        confirmation_form = ConfirmationForm()
    return render(request,'commonuser/confirm.html',
                          {'confirmation_form':confirmation_form,'phone_number':username})

def TwoMinWaitView(request):
    return render(request,'commonuser/wait.html')

def WrongPhoneNumberView(request):
    return render(request,'commonuser/wrongphonenumber.html')


@login_required
def CommonUserProfileView(request,slug):
    user_instance = get_object_or_404(UserModel,slug = slug)
    commonuser_instance = get_object_or_404(CommonUserModel, user = user_instance)
    try:
        orders = get_list_or_404(OrderingModel, user = user_instance)
        if request.user == user_instance:
            return render(request,'commonuser/commonuserprofile.html',
                         {'commonuser_detail':commonuser_instance,'orders':orders})
    except:
        if request.user == user_instance:
            return render(request,'commonuser/commonuserprofile.html',
                         {'commonuser_detail':commonuser_instance})


@login_required
@commonuser_required
def CommonUserUpdateView(request,slug):
    commonuser_user = get_object_or_404(UserModel,slug = slug)
    if request.user == commonuser_user :
        user_update_form = UserUpdateForm(request.POST or None, instance = commonuser_user)
        commonuser = get_object_or_404(CommonUserModel, user = commonuser_user)
        if user_update_form.is_valid():
            user_update_form.save()
            if 'picture' in request.FILES:
               commonuser.picture = request.FILES['picture']
               commonuser.save()
            return HttpResponseRedirect(reverse('commonuser:profile',
                                        kwargs={'slug':commonuser_user.slug}))
        return render(request,'commonuser/commonuserupdate.html',
                              {'userform':user_update_form,})
    else:
        return HttpResponseRedirect(reverse('login'))

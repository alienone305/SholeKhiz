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
import jdatetime
import datetime
import random
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.utils import timezone
# handmade

from delegations.forms import DelegationForm
from delegations.models import DelegationModel
from accounts.decorators import superuser_required
from accounts.forms import ForgotPasswordForm, PasswordChangeForm
from accounts.models import UserModel
from commonuser.models import CommonUserModel
from company.utils import SendMessage

@login_required
@superuser_required
def SuperUserDashboardView(request):
    return render(request,'accounts/superuserdashboard.html')


def ForgotPasswordView(request):
    try:
        last_retry_str = request.session['last_retry']
        last_retry = datetime.datetime.strptime(last_retry_str,"%Y-%m-%d %H:%M:%S")
    except:
        last_retry = datetime.datetime.now()
    now = datetime.datetime.now()
    if now >= last_retry:
        if request.method == 'POST':
            data = request.POST.copy()
            form = ForgotPasswordForm(data=request.POST)

            phone_number_exists = False
            if form.is_valid():
                phone_number = form.cleaned_data.get('phone_number')
                number = '0'+phone_number

                try :
                    user = get_object_or_404(UserModel,username = phone_number)
                    if user :
                        var = 'abcdefghijkmnpqrstuvwxyzABCDEFJKLMNPQRSTUVWXYZ123456789'
                        new_password=''
                        for i in range(0,random.randrange(7,8,1)):
                            c = random.choice(var)
                            new_password += c

                        text = 'رمز عبور جدید شما در وبسایت شعله خیز: {code}\n شعله خیز آذر'.format(code = new_password)
                        SendMessage(number,text)
                        phone_number_exists = True
                        print(new_password)
                        user.set_password(new_password)
                        user.save()
                        now = datetime.datetime.now() + datetime.timedelta(minutes=3)
                        str_now = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
                        request.session['last_retry'] = str_now
                        return HttpResponseRedirect(reverse('accounts:login'))
                except:
                    pass



            else:
                print(form.errors)
            if not phone_number_exists:
                return HttpResponseRedirect(reverse('commonuser:wrongphonenumber'))


        else:
            form = ForgotPasswordForm()
        return render(request,'accounts/forgotpassword.html',{'form':form})
    else:
        return HttpResponseRedirect(reverse('commonuser:wait'))

@login_required
def PasswordChangeView(request,slug):
    user = get_object_or_404(UserModel,slug = slug)
    if request.method == 'POST':
        password_form = PasswordChangeForm(data = request.POST)
        if password_form.is_valid():
            current_password = password_form.cleaned_data.get('current_password')
            logged_in = authenticate(request, username=user.username, password=current_password)

            if logged_in is not None:
                if password_form.cleaned_data.get('new_password') == password_form.cleaned_data.get('confirm_password'):
                    new_password = password_form.cleaned_data.get('new_password')
                    try:
                        user.set_password(new_password)
                        user.save()
                        return HttpResponseRedirect(reverse('accounts:login'))
                    except:
                        error1 ='کلمه عبور باید بیش از 6 کاراکتر باشد'
                        error2 ='کلمه عبور باید نمیتواند شامل نام کاربری باشد'
                        error3 ='کلمه عبور نمیتواند خیلی ساده باشد'
                        return render(request,'accounts/passwordchange.html',{'form':password_form,'error1':error1,'error2':error2,'error3':error3})
                else:
                    error4 = 'رمز های وارد شده با هم مطابقت ندارند'
                    password_form = PasswordChangeForm()
                    return  render(request,'accounts/passwordchange.html',
                                          {'error4':error4,'form':password_form})

            else:
                error4 = 'رمزعبور وارد شده صحیح نیست'
                password_form = PasswordChangeForm()
                return  render(request,'accounts/passwordchange.html',
                                      {'error4':error4,'form':password_form})
    else:
        password_form = PasswordChangeForm()
        return  render(request,'accounts/passwordchange.html',
                              {'form':password_form})

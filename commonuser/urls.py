from django.urls import include, path
from commonuser.views import (CommonUserSignupView, CommonUserProfileView,
                            CommonUserUpdateView, UserConfirmView, TwoMinWaitView,
                            WrongPhoneNumberView,)

app_name ='commonuser'
urlpatterns = [
    path('signup/', CommonUserSignupView, name='signup'),
    path('confirm/',UserConfirmView, name='confirm'),
    path('wait/',TwoMinWaitView, name='twominwait'),
    path('wrong-number/',WrongPhoneNumberView, name='wrongphonenumber'),
    path('profile/<slug:slug>/',CommonUserProfileView, name = 'profile'),
    path('update/<slug:slug>/',CommonUserUpdateView, name = 'update'),

]

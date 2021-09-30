from django.urls import include, path
from django.contrib.auth import views as auth_views
from accounts.forms import UserLoginForm

# handmade
from accounts.views import SuperUserDashboardView, ForgotPasswordView, PasswordChangeView

app_name ='accounts'
urlpatterns = [
    path('auth/',auth_views.LoginView.as_view(template_name='registration/login.html',authentication_form=UserLoginForm), name='login'),
    path('dashboard/',SuperUserDashboardView, name='superuserdashboard'),
    path('forgot-password/',ForgotPasswordView, name='passwordforget'),
    path('change-password/<slug:slug>/',PasswordChangeView, name='passwordchange'),

]

"""SholehKhiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView


urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('',HomeView,name = 'home'),
    path('admin/', admin.site.urls),
    path('superuser/', include('accounts.urls',namespace = 'accounts')),
    path('user/', include('commonuser.urls',namespace = 'commonuser')),
    path('products/', include('products.urls',namespace = 'products')),
    path('company/', include('company.urls',namespace = 'company')),
    path('order/', include('order.urls',namespace = 'order')),
    path('gallery/', include('gallery.urls',namespace = 'gallery')),
    path('delegations/', include('delegations.urls',namespace = 'delegations')),
    path('cooperation/', include('cooperation.urls',namespace = 'cooperation')),
    path('',include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

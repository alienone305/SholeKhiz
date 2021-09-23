from django.urls import include, path
from company.views import (ContactUsView, AboutUsView, ContactUsListView,
                            ContactUsDeleteView)

app_name ='company'
urlpatterns = [
    path('about-us/',AboutUsView, name = 'about-us'),
    path('contact-us/',ContactUsView, name = 'contact-us'),
    path('contact-us-list/',ContactUsListView, name = 'contact-us-list'),
    path('contact-us-delete/<int:pk>',ContactUsDeleteView, name = 'contact-us-delete'),

]

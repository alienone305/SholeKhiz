from django.urls import include, path
from delegations.views import (AddDelegationView, DelegationsListViewSuperUser,
                                DelegationUpdateView, DelegationDeleteView,
                                DelegationsPublicList)

app_name ='delegations'
urlpatterns = [
    path('add/', AddDelegationView, name='add'),
    path('list/', DelegationsListViewSuperUser, name='listsuperuser'),
    path('update/<int:pk>/', DelegationUpdateView, name='update'),
    path('delete/<int:pk>/', DelegationDeleteView, name='delete'),
    path('publiclist/', DelegationsPublicList, name='publiclist'),

]

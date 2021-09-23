from django.urls import include, path
from order.views import (OrderingView, CheckedOrdersListView, OrdersDetailView,
                        UnCheckedOrdersListView, OrdersChangeStatus)

app_name ='ordering'
urlpatterns = [
    path('ordering/<int:pk>/', OrderingView, name='order'),
    path('checked-list/', CheckedOrdersListView, name='checkedlist'),
    path('unchecked-list/', UnCheckedOrdersListView, name='uncheckedlist'),
    path('detail/<int:pk>/', OrdersDetailView, name='detail'),
    path('change-status/<int:pk>/', OrdersChangeStatus, name='changestatus'),


]

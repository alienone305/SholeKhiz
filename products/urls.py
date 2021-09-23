from django.urls import include, path
from products.views import (CreateProductView, ProductsListViewSuperUser,
                            ProductsDeleteView, ProductsUpdateView,
                            TowerDryerListView, PackageListView,
                            RadiatorListView, WaterHeaterListView)

app_name ='products'
urlpatterns = [
    path('create/', CreateProductView, name='create'),
    path('list-superuser/', ProductsListViewSuperUser, name='listsuperuser'),
    path('delete/<int:pk>/', ProductsDeleteView, name='delete'),
    path('update/<int:pk>/', ProductsUpdateView, name='update'),
    path('towerdryer-list/', TowerDryerListView, name='towerdryerlist'),
    path('package-list/', PackageListView, name='packagelist'),
    path('radiator-list/', RadiatorListView, name='radiatorlist'),
    path('waterheater-list/', WaterHeaterListView, name='waterheaterlist'),

]

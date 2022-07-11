from . import views
from django.urls import path, include

urlpatterns = [
    path('',
         views.PrimeAccessView.as_view(),
         name="PrimeAccessView"),
    path('all-products/<category>/',
         views.AllProductsView.as_view(),
         name="AllProductsView"),
    path('add-products/',
         views.AddProductsView.as_view(),
         name="AddProductsView"),
    path('all-orders/<category>/',
         views.AllOrdersView.as_view(),
         name="AllOrdersView"),
    path('delivery-settings/',
         views.DeliverySettings.as_view(),
         name="DeliverySettingsView"),
    path('delivery-settings/<action>/<instance>/',
         views.ModifyDeliverySettings.as_view(),
         name="DeliverySettingsModificationView"),
]

from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('',
         views.PrimeAccessView.as_view(),
         name="PrimeAccessView"),

    path('all-colors/',
         views.AllColorsView.as_view(),
         name="AllColorsView"),
    path('all-colors/<action>/<instance>/',
         views.ModifyColorsView.as_view(),
         name="ModifyColorsView"),

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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
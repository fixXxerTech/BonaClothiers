from . import views
from django.urls import path, include

urlpatterns = [
    path('',
         views.HomePageView.as_view(),
         name="HomePageView"),
    path('order/',
         views.OrderPageView.as_view(),
         name="OrderPageView"),
    path('pay/',
         views.PaymentPageView.as_view(),
         name="PaymentPageView"),
]

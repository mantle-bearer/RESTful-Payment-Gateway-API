from django.urls import path
from .views import PaymentInitiateView, PaymentStatusView

urlpatterns = [
    path('api/v1/payments', PaymentInitiateView.as_view(), name='payment-initiate'),
    path('api/v1/payments/<str:reference>', PaymentStatusView.as_view(), name='payment-status'),
]

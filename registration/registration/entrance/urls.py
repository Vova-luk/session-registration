from django.urls import path
from .views import Confirmation, Glavnaya, Index, Registration

urlpatterns = [
    path('',Index.as_view(), name='index'),
    path('reg/', Registration.as_view(),name='reg'),
    path('mail_confirmation/', Confirmation.as_view(), name='mail_confirmation'),
    path('glavnaya/', Glavnaya.as_view(), name='glavnaya')
]
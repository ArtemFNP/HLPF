from django.urls import path
from . import views

urlpatterns = [
    path('', views.currency_list, name='currency_list'),
]

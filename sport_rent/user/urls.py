from django.urls import path, include
from .views import *

urlpatterns = [
    path('create', UserCreate.as_view(), name='user_create'),
    path('create/city', CityView.as_view(), name='city_ajax_url'),
    path('<pk>/', UserDetail.as_view(), name='user_url'),
]
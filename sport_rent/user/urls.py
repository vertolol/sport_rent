from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    # path('registration', UserCreate.as_view(), name='user_registration'),
    path('create/city', CityView.as_view(), name='city_ajax_url'),
    path('<pk>/', UserDetail.as_view(), name='user_url'),
]
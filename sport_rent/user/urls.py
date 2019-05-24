from django.urls import path, include
from .views import UserDetail

urlpatterns = [
    path('<pk>', UserDetail.as_view(), name='user_url'),
]
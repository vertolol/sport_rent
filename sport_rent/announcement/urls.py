

from django.urls import path, include
from .views import ann_list

urlpatterns = [
    path('', ann_list),
]


from django.urls import path, include
from .views import ann_list, ann_detail

urlpatterns = [
    path('', ann_list, name='ann_list_url'),
    path('ann/<slug>/', ann_detail, name='ann_detail_url'),
]
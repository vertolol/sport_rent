
from django.urls import path, include
from .views import AnnouncementList, AnnouncementDetail

urlpatterns = [
    path('', AnnouncementList.as_view(), name='ann_list_url'),
    path('ann/<slug>/', AnnouncementDetail.as_view(), name='ann_detail_url'),
]
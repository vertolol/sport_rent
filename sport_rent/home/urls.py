from django.urls import path, include
from .views import CategoryDetail, HomePage


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<slug>/', CategoryDetail.as_view(), name='category_url')
]

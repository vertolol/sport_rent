
from django.urls import path, include
from .views import home_page, category

urlpatterns = [
    path('', home_page, name='home'),
    path('<slug>', category, name='category_url')
]

from .models import UserProfile
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, View
# from .forms import UserForm
from cities_light.models import Region, City


class UserDetail(DetailView):

    model = UserProfile
    template_name = 'user/user.html'
    context_object_name = 'user'


class CityView(View):

    def get(self, request):
            id_region = int(request.GET['id_region'])
            cities = Region.objects.get(id=id_region).city_set.all()
            return render(request, 'user/city.html', context={'cities' : cities})

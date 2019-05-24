from .models import UserProfile
from django.views.generic import DetailView


class UserDetail(DetailView):

    model = UserProfile
    template_name = 'user/user.html'
    context_object_name = 'user'
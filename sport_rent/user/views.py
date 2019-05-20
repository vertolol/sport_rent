from django.shortcuts import render
from .models import UserProfile
# Create your views here.

def user(request, pk):

    context = {
        'user': UserProfile.objects.get(pk__iexact=pk)
    }
    return render(request, 'user/user.html', context=context)
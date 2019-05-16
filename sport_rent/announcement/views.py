from django.shortcuts import render
from .models import Announcement

def ann_list(request):
    context = {
        'anns': Announcement.objects.all(),
    }
    return render(request, 'ann/ann_list.html', context=context)

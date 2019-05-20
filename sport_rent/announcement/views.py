from django.shortcuts import render
from .models import Announcement

def ann_list(request):
    context = {
        'anns': Announcement.objects.all(),
    }
    return render(request, 'ann/ann_list.html', context=context)


def ann_detail(request, slug):
    context = {
        'ann': Announcement.objects.get(slug__iexact=slug)
    }
    return render(request, 'ann/ann_detail.html', context=context)

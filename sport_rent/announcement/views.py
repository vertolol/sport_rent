from .models import Announcement
from django.views.generic import ListView, DetailView


class AnnouncementList(ListView):

    model = Announcement
    template_name = 'ann/ann_list.html'
    context_object_name = 'anns'


class AnnouncementDetail(DetailView):

    model = Announcement
    template_name = 'ann/ann_detail.html'
    context_object_name = 'ann'


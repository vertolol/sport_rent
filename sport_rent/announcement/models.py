from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model


class Announcement(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = AutoSlugField(populate_from='title',
                         unique=True)
    description = models.TextField(blank=True, db_index=True)
    # selling_price = models.IntegerField()
    # rental_price = models.IntegerField()
    # image = models.ImageField()
    date_pub = models.DateTimeField(default=timezone.now)
    # category = models.ForeignKey('home.Category', on_delete=models.CASCADE, related_name='announcements')
    # city = models.CharField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='announcements')

    def get_absolute_url(self):
        return reverse('ann_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


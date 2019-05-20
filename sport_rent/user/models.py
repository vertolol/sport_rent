from django.db import models
# from autoslug import AutoSlugField
from django.utils import timezone
from django.urls import reverse
from cities_light.models import City


class UserProfile(models.Model):
    first_name = models.CharField(max_length=150, db_index=True)
    # last_name = models.CharField(max_length=150, db_index=True)
    # slug = models.SlugField(blank=True, null=True)
    # phone =
    # email =
    # vk =
    # avatar = models.ImageField()
    date_create_profile = models.DateTimeField(default=timezone.now)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='users')

    @property
    def city_name(self):
        return self.city.alternate_names.split(';')[-1]

    def region_name(self):
        return self.city.region.alternate_names.split(';')[-1]

    def get_absolute_url(self):
        return reverse('user_url', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name
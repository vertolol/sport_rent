from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from autoslug import AutoSlugField
from django.urls import reverse


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = AutoSlugField(populate_from='name',
                         unique=True)


    class MPTTMeta:
        order_insertion_by = ['-tree_id']

    def get_absolute_url(self):
        return reverse('category_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
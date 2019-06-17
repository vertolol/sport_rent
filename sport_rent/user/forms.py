from django import forms
from cities_light.models import Region, City
from .models import UserProfile


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    # last_name = models.CharField(max_length=150, db_index=True)
    # slug = models.SlugField(blank=True, null=True)
    # phone =
    # email =
    # vk =
    # avatar = models.ImageField()
    # date_create_profile = forms.DateTimeField(default=timezone.now)

    city = forms.ChoiceField(label="city",
                             # choices=[(i.pk, i.alternate_names) for i in City.objects.all()],
                             required=True)

    region = forms.ChoiceField(label="region",
                               choices=sorted(
                                    [(i.id, i.alternate_names.split(';')[-1]) for i in Region.objects.all()],
                                    key=lambda x: x[1]),
                               required=True)

    class Meta():
        model = UserProfile
        fields = (
            'first_name', 'region', 'city',
        )

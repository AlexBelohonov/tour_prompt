from django.db import models
from django.utils.translation import gettext_lazy as _

from tour_prompt.mixins import UpdateCreateMixin


class Tour(UpdateCreateMixin):
    city = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    venue = models.CharField(max_length=254, blank=True, null=True)
    date = models.DateField()
    link = models.URLField(max_length=200, blank=True, null=True)
    tickets_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.city}_{self.country}'

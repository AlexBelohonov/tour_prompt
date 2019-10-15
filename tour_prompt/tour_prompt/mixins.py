from django.db import models


class UpdateCreateMixin(models.Model):
    """
    Mixin to have created_at, updated_at fields
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

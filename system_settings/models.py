from django.db import models
import uuid

from user.models import UserDetails


class EmailSettings(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True, blank=True)
    is_enabled = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Email Settings'

    def __str__(self):
        return self.user.full_name


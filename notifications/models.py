from django.db import models

from user.models import GuestUsers
from properties.models import Properties
import uuid


class Notifications(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(GuestUsers, on_delete=models.CASCADE, null=True, blank=True)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return str(self.user.full_name)


class NotificationQueue(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    notification = models.ForeignKey(Notifications, on_delete=models.CASCADE, null=True, blank=True)
    email_notified = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Notification Queue'

    def __str__(self):
        return str(self.notification.user.full_name)
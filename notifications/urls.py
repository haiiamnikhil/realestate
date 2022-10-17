from django.views.generic import TemplateView
from django.urls import path

from notifications.views.user import send_message_notifications

urlpatterns = [
    path('create/', send_message_notifications.SendMessageUser.as_view(), name='send_message_user'),
]
from django.shortcuts import render
from django.views import generic

from notifications.models import Notifications


class NotificationDetailsAdmin(generic.DetailView):
    template_name = 'notifications/admin/notification_details.html'

    def get(self, request, uid):
        context = self.get_context(uid)
        return render(request,self.template_name,context)

    def get_context(self, uid):
        params = {}
        params['notification'] = Notifications.objects.get(uid=uid)
        return params
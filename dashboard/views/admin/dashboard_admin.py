from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from user.models import UserDetails
from properties.models import Properties


@method_decorator(login_required, name="dispatch")
class DashboardView(View):
    template_name = 'dashboard/admin/admin_dashboard.html'

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)

    def get_context(self):
        params = {}
        params['properties'] = self.get_property_details()
        return params

    def get_property_details(self):
        params = {}
        properties = Properties.objects
        params['total_properties'] = properties.all().count()
        params['sold'] = properties.filter(status='sold').count()
        params['active'] = properties.filter(status='active').count()
        params['cancelled'] = properties.filter(status='cancel').count()

        return params
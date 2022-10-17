from django.shortcuts import render
from django.views import generic

from properties.models import Properties


class PropertyDetailsUser(generic.DetailView):
    template_name = 'properties/user/property_details.html'

    def get(self, request, slug,uid):
        context = self.get_context(uid)
        return render(request,self.template_name,context)

    def get_context(self, uid):
        params = {}
        params['property'] = Properties.objects.get(uid=uid)
        return params
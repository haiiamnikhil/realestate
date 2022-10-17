from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import generic

from properties.models import Properties


class SearchFilterPropertiesUser(generic.ListView):
    template_name = 'properties/user/list_properties_ajax.html'

    def get(self, request):
        context = self.get_context()
        print(context)
        render = render_to_string(self.template_name,context)
        return JsonResponse(render,safe=False,status=200)

    def get_context(self):
        params = {}
        params['properties'] = Properties.objects.all().order_by('-created_at')
        return params
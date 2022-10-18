from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render

from properties.models import Properties


@method_decorator(login_required, name="dispatch")
class EditPropertiesAdmin(generic.UpdateView):
    template_name = 'properties/admin/edit_property.html'

    def get(self, request, uid):
        context = self.get_context(uid)
        return render(request, self.template_name, context)


    def get_context(self, uid):
        params = {}
        params['property'] = Properties.objects.get(uid=uid)
        return params
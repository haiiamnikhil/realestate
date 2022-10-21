from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from user.models import UserDetails
from system_settings.models import EmailSettings
from utils.common.response.response import ResponseGenerator


@method_decorator(login_required, name="dispatch")
@method_decorator(csrf_exempt, name="dispatch")
class SystemSettingsConfig(generic.ListView):
    template_name='system_settings/admin/settings.html'
    
    def get(self, request):
        context = self.get_context(request)
        print(context)
        return render(request, self.template_name, context)

    def get_context(self, request):
        params = {}
        user = UserDetails.objects.get(user=request.user)
        try:
            email = EmailSettings.objects.get(user=user)
            params['email'] = email
        
        except EmailSettings.DoesNotExist:
            pass

        return params